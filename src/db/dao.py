from sqlalchemy import insert, text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession

from core import schemes
from db import models
from db.engine import connection


from logger import setup_logger
logger = setup_logger(__name__)


@connection(commit=True)
async def create_creator(session: AsyncSession, id: int):
    try:
        await session.execute(insert(models.Creator).values(id=id))
    except IntegrityError as e:
        pass
    except DBAPIError as e:
        logger.warning(f"Fail to insert creator with id={id}")


@connection(commit=True)
async def create_video(session: AsyncSession, video: schemes.Video):
    try:
        await session.execute(insert(models.Video).values(**video.model_dump()))
    except SQLAlchemyError:
        logger.warning(f"Fail to insert video item: {video}")


@connection(commit=True)
async def create_snapshot(session: AsyncSession, snapshot: schemes.SnapShot):
    try:
        await session.execute(insert(models.SnapShot).values(**snapshot.model_dump()))
    except SQLAlchemyError:
        logger.warning(f"Fail to insert snapshot item: {snapshot}")


@connection()
async def info_message(session: AsyncSession, sql: str):

    try:
        return (await session.execute(text(sql))).scalar_one_or_none()
    except SQLAlchemyError as e:
        logger.warning(f"Fail to execute query: {sql}")
    