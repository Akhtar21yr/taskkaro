from sqlmodel import create_engine,SQLModel,Session
from pathlib import Path
from typing import Annotated
from fastapi import Depends


BASE_DIR = Path(__name__).resolve().parent
DB_PATH = BASE_DIR / 'sqlite.db'
DB_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(DB_URL,echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)
    
    
def get_session():
    with Session(engine) as session :
        yield session
        
        
SessionDep = Annotated[Session,Depends(get_session)]