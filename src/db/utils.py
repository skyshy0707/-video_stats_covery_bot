from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeMeta

def model_to_str(model: DeclarativeMeta) -> str:
    fstr = \
    f"""
    class {model.__class__.__name__}:\n
        \t__tablename__ = {model.__tablename__}\n
    """

    for column in inspect(model).columns:
        fstr += f"\t{column.name}\n"
    
    return fstr