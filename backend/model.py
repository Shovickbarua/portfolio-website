from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True)
    email = Column(String(255), unique=True, index=True)
    message = Column(String(255), unique=True, index=True)

