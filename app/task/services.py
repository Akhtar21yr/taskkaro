from app.db.config import engine
from app.task.models import Task
from sqlmodel import Session,select
from app.task.models import *

def create_task(new_task:TaskCreate) -> TaskOut:
    with Session(engine)  as sesion:
        task = Task(new_task)
        sesion.add(task)
        sesion.commit()
        sesion.refresh(task)
        return task
    
def get_all_task() -> TaskOut:
    with Session(engine) as session:
        stmt = select(Task)
        tasks = session.exec(stmt).all()
        return tasks
    
def get_task_by_id(id:int) -> TaskOut:
    with Session(engine) as session:
        task = session.get_one(Task,id)
        return task
    
def update_task(id:int,new_task:TaskUpdate) -> TaskOut: 
    with Session(engine) as session:
        task = session.get_one(Task,id)
        task.title = new_task.title
        task.content = new_task.content
        session.commit()
        session.refresh(task)
        return task
    
def delete_task(id:int) -> bool:
    with Session(engine) as session:
        task = session.get_one(Task,id)
        session.delete(task)
        session.commit()
        return True
    
    