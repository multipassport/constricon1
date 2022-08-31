from fastapi import FastAPI

from .db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
