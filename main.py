from sqlalchemy import create_engine,Column,Integer,Boolean,String
from sqlalchemy.orm import sessionmaker, Session,declarative_base
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# database url 
DATABASE_URL = "sqlite:///./test.db"

# create database 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# create temporary session for database operation 
sessionLocal = sessionmaker(bind=engine)

# create Base for Database's  Table
Base = declarative_base()

# create Table model
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean)

# create table
Base.metadata.create_all(bind=engine)

# Dependency Injection that will provide session 
def get_db():
    db = sessionLocal()
    try:
        yield db                     # means it provide session to fastapi
    finally:
        db.close()

# CRUD Operations 
# Create api for inserting data into the database tabel
@app.post("/todos")
def create_todos(title:str,db:Session=Depends(get_db)):
    todo = Todo(title=title,completed=False)       # This is a way to insert data into the table 
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Created",
        "Data":todo
    }

# All Data Read Operation
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todo = db.query(Todo).all()
    return {
        "Total":len(todo),
        "Data":todo
    }

# Read Data based on ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404, 
            detail="Todo not found"
        )
    return todo

# update the data 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,completed:bool,title:str,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    todo.title = title
    todo.completed = completed
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Updated",
        "Data":todo
    }

# Delete the data
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    db.delete(todo)
    db.commit()
    return {
        "message":"Todo Deleted"
    }