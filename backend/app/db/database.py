from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..config import settings


SQLALCHEMY_DATABASE_URL = settings.postgres_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
