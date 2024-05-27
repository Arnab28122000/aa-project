import os
from sqlmodel import create_engine, Session, SQLModel

db_url = os.environ['DATABASE_URL']

DATABASE_URL = db_url

engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # Increase pool size
    max_overflow=20,      # Increase overflow limit
    pool_timeout=30,      # Set the pool timeout (default is 30 seconds)
    pool_recycle=1800     # Recycle connections after 30 minutes
)

def get_session() -> Session:
   return Session(engine)

# Function to initialize the database and create all tables
def init_db():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(e)