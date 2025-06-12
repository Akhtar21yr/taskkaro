from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_table,SessionDep
from app.task import services as task_services
from app.task.models import *

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table()
    yield
    
app = FastAPI(lifespan=lifespan) 

@app.get('/task',response_model=TaskOut|list[TaskOut])
def get_task(session:SessionDep,id:int|None=None):
    return task_services.get_task_by_id(session,id=id) if id else task_services.get_all_task(session)

@app.post('/task',response_model=TaskOut)
def create_task(session:SessionDep,new_task:TaskCreate):
    print('>>>>>>>>Task',new_task)
    return task_services.create_task(session,new_task)

@app.put('/task/{task_id}',response_model=TaskOut)
def update_task(session:SessionDep,task_id:int,new_task:TaskUpdate):
    return task_services.update_task(session,id=task_id,new_task=new_task)

@app.delete('/task/{task_id}')
def delete_task(session:SessionDep,task_id:int):
    return {'deleted':task_services.delete_task(session,task_id)}