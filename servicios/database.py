# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLite engine
engine = create_engine('sqlite:///game.db', echo=True)

# Create a base class for ORM models
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        return db

def create_tables():
    Base.metadata.create_all(engine)