database_url="postgresql://postgres:postgres@localhost:5432/pos_db"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(database_url, echo=False,future=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
