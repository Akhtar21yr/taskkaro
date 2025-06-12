from app.db.config import engine
from app.task.models import Task
from sqlmodel import Session,select
from app.task.models import *

def create_task(session:Session,new_task:TaskCreate) -> TaskOut:
        task = Task(title=new_task.title,content=new_task.content)
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    
def get_all_task(session:Session,) -> TaskOut:
        stmt = select(Task)
        tasks = session.exec(stmt).all()
        return tasks
    
def get_task_by_id(session:Session,id:int) -> TaskOut:
        task = session.get_one(Task,id)
        return task
    
def update_task(session:Session,id:int,new_task:TaskUpdate) -> TaskOut: 
        task = session.get_one(Task,id)
        task.title = new_task.title
        task.content = new_task.content
        session.commit()
        session.refresh(task)
        return task
    
def delete_task(session:Session,id:int) -> bool:
    
        task = session.get_one(Task,id)
        session.delete(task)
        session.commit()
        return True
    
    