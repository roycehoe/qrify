import functools
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "postgresql://royce:password@db/card_game"
SQLALCHEMY_DATABASE_URL = "postgresql://royce:password@localhost:5432/card_game"
SQLALCHEMY_DATABASE_URL = "postgresql://royce:password@db/card_game"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(
    autoflush=False, bind=engine, expire_on_commit=False, autocommit=True
)

Base = declarative_base()


def get_session() -> Generator:
    """Creates a database session"""

    session = SessionLocal()
    try:
        session.begin()
        yield session
    finally:
        session.close()
