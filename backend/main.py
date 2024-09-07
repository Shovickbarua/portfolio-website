from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Union, Annotated
from backend import model
from backend.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Adjust this list with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


class UserBase(BaseModel):
    name : str
    email : str
    message : str

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def get_users(db: db_dependency):
    # users = db.query(model.User).all()
    # return users
    return {"message": "Hello World"}

@app.post("/users")
async def post_users(user: UserBase, db: db_dependency):
    user = model.User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

