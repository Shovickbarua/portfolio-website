from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Union, Annotated
from . import model
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
model.Base.metadata.create_all(bind=engine)


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

@app.get("/users")
async def get_users(db: db_dependency):
    users = db.query(model.User).all()
    return users

@app.post("/users")
async def post_users(user: UserBase, db: db_dependency):
    user = model.User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

