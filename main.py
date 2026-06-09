# Import the required packages
from sqlalchemy import create_engine, Integer, String, BOOLEAN, Column
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI, Depends

# create FastAPI object
app = FastAPI()


# Database path
DATABASE_URL = "sqlite:///./test.db"

# This is used to connect the database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Create a temporary Session for database
sessionLocal = sessionmaker(bind=engine)

# This is the parent class/base for all database tables.
Base = declarative_base()

# define table
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    completed = Column(BOOLEAN)

# Creating the table
Base.metadata.create_all(bind=engine)

# Declare a function
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# create /database route
@app.get("/database")
def database(db:Session = Depends(get_db)):
    return {
        "message":"DATABASE Connected Successfully"
    }



