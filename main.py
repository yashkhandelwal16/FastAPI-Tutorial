from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import model,schemas
from auth import create_token,verify_token

model.base.metadata.create_all(bind=engine)

app = FastAPI()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Login API 
@app.post("/login")
def login():
    return {
        "access_token":create_token({"user":"admin"}),
        "token_type":"bearer"
    }

# Home API 
@app.get("/")
def home():
    return {
        "message":"Blog API Started"
    }

# Created Blog (Protected)
@app.post("/blogs",response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate,db:Session=Depends(get_db),user=Depends(verify_token)):
    new_blog = model.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Read All Blog 
@app.get("/blogs")
def get_blogs(page:int=1,limit:int=5,search:str=Query(default=""),db:Session=Depends(get_db)):
    query = db.query(model.Blog)
    if search:
        query = query.filter(model.Blog,title.ilike(f"%{search}%"))
    total = query.count()
    start = (page-1)*limit
    blogs = query.offset(start).limit(limit).all()

    return{
        "page":page,
        "limit":limit,
        "total":total,
        "data":blogs
    }

# Read One Blog 
@app.get("/blogs/{id}",response_model=schemas.BlogResponse)
def get_blog(id:int,db:Session=Depends(get_db)):
    blog = db.query(model.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog Not Found"
        )
    return blog

# Update Blog API (Protected)
@app.put("/blogs/{id}",response_model=schemas.BlogResponse)
def update_blog(id:int,blog:schemas.BlogCreate,db:Session=Depends(get_db),user=Depends(verify_token)):
    existing_blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not existing_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog Not Found"
        )
    existing_blog.title = blog.title
    existing_blog.content = blog.content
    db.commit()
    return existing_blog

# Delete Blog API (Protected)
@app.delete("/blogs/{id}")
def delete_blog(id:int,db:Session=Depends(get_db),user=Depends(verify_token)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog Not Found"
        )
    blog.delete()
    db.commit()

    return {
        "message":"Blog Deleted Successfully"
    }




