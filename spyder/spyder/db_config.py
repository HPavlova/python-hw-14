from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite3:///spiders.db'

engine = create_engine(DB_URL, echo=True)
