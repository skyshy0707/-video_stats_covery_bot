from functools import wraps

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import  registry
from sqlalchemy import AsyncAdaptedQueuePool

from config import db
from logger import setup_logger

logger = setup_logger(__name__)
mapper = registry()

Base = mapper.generate_base()

DB_URL = URL.create(
    "postgresql+asyncpg",
    username=db.POSTGRES_DB_USER,
    password=db.POSTGRES_DB_PASSWORD,
    host=db.POSTGRES_DB_HOST,
    database=db.POSTGRES_DB_NAME
)

engine = create_async_engine(
    DB_URL,
    echo=False,
    future=True,
    pool_size=75,
    max_overflow=100,
    pool_recycle=200,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool
)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def connection(commit=False):
    def _connection(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with async_session_maker() as session:
                async with session.begin():
                    result = await func(session, *args, **kwargs)  
                    if commit:
                        await session.commit()
                    return result
        return wrapper
    return _connection