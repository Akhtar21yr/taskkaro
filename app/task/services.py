from app.db.config import engine
from app.task.models import Task
from sqlmodel import Session,select

def create_task(title:str,content:str):
    with Session(engine)  as sesion:
        task = Task(title=title,content=content)
        sesion.add(task)
        sesion.commit()
        sesion.refresh(task)
        return task
    
def get_all_task():
    with Session(engine) as session:
        stmt = select(Task)
        tasks = session.exec(stmt).all()
        return tasks
    
def get_task_by_id(id:int):
    with Session(engine) as session:
        task = session.get_one(Task,id)
        return task
    
def update_task(id:int,title:str,content:str):
    with Session(engine) as session:
        task = session.get_one(Task,id)
        task.title = title
        task.content = content
        session.commit()
        session.refresh(task)
        return task
    
def delete_task(id:int):
    with Session(engine) as session:
        task = session.get_one(Task,id)
        session.delete(task)
        session.commit()
        return True
    
    