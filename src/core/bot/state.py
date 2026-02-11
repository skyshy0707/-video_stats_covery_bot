from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    answer_to_user = State()