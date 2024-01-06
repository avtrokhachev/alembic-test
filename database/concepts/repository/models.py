import typing as tp

from sqlalchemy import CursorResult, create_engine
from sqlalchemy import Engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Repository:
    _engine: tp.Optional[Engine] = None

    @classmethod
    def run(cls, *args, **kwargs) -> CursorResult:
        engine = cls._get_engine()
        with engine.begin() as conn:
            result = conn.execute(*args, **kwargs)

        return result

    @classmethod
    def _get_engine(cls) -> Engine:
        if cls._engine is None:
            cls._engine = create_engine("postgresql://localhost:5432/avtrokhachev")

        return cls._engine
