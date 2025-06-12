from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_table
from app.task import services as task_services
from app.task.models import *

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table()
    yield
    
app = FastAPI(lifespan=lifespan) 

@app.get('/task',response_model=TaskOut|list[TaskOut])
def get_task(id:int|None=None):
    return task_services.get_task_by_id(id=id) if id else task_services.get_all_task()

@app.post('/task',response_model=TaskOut)
def create_task(new_task:TaskCreate):
    print('>>>>>>>>Task',new_task)
    return task_services.create_task(new_task)

@app.put('/task/{task_id}',response_model=TaskOut)
def update_task(task_id:int,new_task:TaskUpdate):
    return task_services.update_task(id=task_id,title=new_task.get('title'),content=new_task.get('title'))

@app.delete('/task/{task_id}',response_model=TaskOut)
def delete_task(task_id:int):
    return {'deleted':task_services.delete_task(task_id)}