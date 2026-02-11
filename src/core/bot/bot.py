from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import app


class TgBot:

    def __init__(self):
        self.__bot = Bot(app.TG_BOT_TOKEN)
        self.__storage = MemoryStorage()
        self.__dispatcher = Dispatcher(storage=self.__storage)
    
    def get_dispatcher(self) -> Dispatcher:
        return self.__dispatcher
    
    def get_bot(self) -> Bot:
        return self.__bot