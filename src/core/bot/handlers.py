from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from mistralai import Mistral

from config import app
from core.bot import templates
from core.bot.state import Form
from db.dao import info_message
from db.models import Creator, Video, SnapShot
from db.utils import model_to_str
from logger import setup_logger

router = Router()

logger = setup_logger(__name__)


@router.message(F.text == '/start')
async def start_bot(message: types.Message, state: FSMContext):
    await message.answer(templates.start_message, parse_mode="html")
    await state.set_state(Form.answer_to_user)

@router.message(Form.answer_to_user)
async def answer_to_user(message: types.Message, state: FSMContext):
    
    llmq = """
    сгенерируйте Sql запрос: {message}. "\
    
    Описания моделей следующие:
    \n
    """
    if message:
        try:
            llmq = llmq.format(message=message.text)
        except Exception as e:
            message.answer("Something went wrong")
   
    llmq = "".join([
        llmq,
        model_to_str(Creator),
        model_to_str(Video),
        model_to_str(SnapShot)
    ])

    with Mistral(api_key=app.MISTRAL_API_KEY) as mistral:
        response = mistral.chat.complete(
            model="codestral-latest",
            messages=[
                {
                    "content": llmq,
                    "role": "user"
                }
            ], 
            stream=False
        )

        sql = response.choices[0].message.content\
            .split("sql")[1]\
            .split("```")[0]\
            .replace("\n", " ")\
            .strip().replace("  ", " ")
        
        logger.info(f"SQL {sql} RETRIEVED SUCCESSFULLY")

        assert all(op not in sql for op in ["ALTER", "DELETE", "INSERT", "UPDATE"])
        number = await info_message(sql)
        logger.info(f"Number: {number}")
        
        await message.answer(
            text=templates.info_message.format(value=number),
            parse_mode="HTML"
        )