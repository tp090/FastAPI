from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


QLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# Replace with your real connection string
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:Admin%40thongdy090@db.dvxmpvzsbbalwfxwvhis.supabase.co:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



