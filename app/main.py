from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_table
from app.task import services as task_services

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table()
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get('/task')
def get_task(id:int|None=None):
    
    return task_services.get_task_by_id(id=id) if id else task_services.get_all_task()

@app.post('/task')
def create_task(new_task:dict):
    return task_services.create_task(title=new_task.get('title'),content=new_task.get('title'))

@app.put('/task/{task_id}')
def update_task(task_id:int,new_task:dict):
    return task_services.update_task(id=task_id,title=new_task.get('title'),content=new_task.get('title'))

@app.delete('/task/{task_id}')
def delete_task(task_id:int):
    return {'deleted':task_services.delete_task(task_id)}