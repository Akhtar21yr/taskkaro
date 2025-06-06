from sqlmodel import create_engine,SQLModel
from pathlib import Path


BASE_DIR = Path(__name__).resolve().parent
DB_PATH = BASE_DIR / 'sqlite.db'
DB_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(DB_URL,echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)