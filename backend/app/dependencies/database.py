from ..db.database import Session


def get_database():
    database = Session()
    try:
        yield database
    finally:
        database.close()
