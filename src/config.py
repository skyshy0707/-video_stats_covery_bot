import os

from pydantic import BaseModel


class Database(BaseModel):

    POSTGRES_DB_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_DB_NAME: str = os.getenv("POSTGRES_DB")

class App(BaseModel):
    
    TG_BOT_TOKEN: str = os.getenv("TG_BOT_TOKEN")
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY")


app = App()
db = Database()