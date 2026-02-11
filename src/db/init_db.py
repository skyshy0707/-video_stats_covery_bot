import asyncio
import time

from asyncpg.exceptions import CannotConnectNowError, InvalidCatalogNameError
from sqlalchemy.exc import OperationalError

from logger import setup_logger
from db.engine import engine
from db.models import Base


logger = setup_logger(__name__)
TIMEOUT = 2

async def create_db():

    while True:
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

        except ConnectionRefusedError as e:
            logger.warning(f"CONNECTION ERROR: {e}")
            time.sleep(TIMEOUT)
            continue
        except CannotConnectNowError as e:
            logger.warning(f"CANNOT CONNECT: {e}")
            time.sleep(TIMEOUT)
            continue
        except RuntimeError as e:
            logger.warning(f"CONNECTION ERROR. DETAILS: {e}. TRY TO RE-CONNECT AGAIN...")
            time.sleep(TIMEOUT)
            continue
        except InvalidCatalogNameError as e:
            logger.warning(f"DATABASE HASN'T CREATED YET {e}")
            time.sleep(TIMEOUT)
            continue
        except OperationalError as e:
            logger.critical(f"OPERATION WAS ENDED WITH AN ERROR: {e}")
            break
        else:
            logger.info("CONNECTION SUCCESS")
            break

if __name__ == "__main__":
    asyncio.run(create_db())