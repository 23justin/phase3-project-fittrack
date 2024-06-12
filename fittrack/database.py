# fittrack/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fittrack.db.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Adjust as per your setup

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
