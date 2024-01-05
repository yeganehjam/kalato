from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from schemas import UserCreate, UserUpdate, AdCreate, AdUpdate
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email_address = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    profile_picture = Column(String)
    password = Column(String)
    user_type = Column(String, index=True)
    username = Column(String, unique=True, index=True)


class Ad(Base):
    __tablename__ = "ads"
    ad_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    date_posted = Column(String)
