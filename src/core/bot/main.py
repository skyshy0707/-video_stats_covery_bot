import asyncio
import time

from aiogram.types import BotCommand, BotCommandScopeDefault
from requests.exceptions import RequestException

from core.bot.bot import TgBot
from core.bot import handlers
from logger import setup_logger

logger = setup_logger(__name__)

tg_bot = TgBot() 
bot = tg_bot.get_bot()
dp = tg_bot.get_dispatcher()


async def setup():
    commands = [BotCommand(command="start", description="Start")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

POLLING_TIMEOUT = 10

async def main():
    dp.include_router(handlers.router)
    dp.startup.register(setup)

    while True:

        try:
            await dp.start_polling(
                bot,
                polling_timeout=POLLING_TIMEOUT
            )

            logger.info("Bot started")
        
        except RequestException as e:
            logger.warning(f"Connection is broke. Details: {e}. Need to wait 30 seconds...")
            time.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
