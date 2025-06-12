from sqlmodel import SQLModel,Field

class TaskBase(SQLModel):
    title :str
    content :str
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass 

class TaskOut(TaskBase):
    id : int = Field(primary_key=True)


class Task(TaskBase,table=True):
    id : int = Field(primary_key=True)