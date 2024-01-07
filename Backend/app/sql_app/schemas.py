from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    profile_picture: str
    password: str
    user_type: str
    username: str
    
class User(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    profile_picture: str
    password: str
    user_type: str
    username: str

class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    profile_picture: str
    password: str
    user_type: str
    username: str

class AdCreate(BaseModel):
    title: str
    description: str
    price: int
    date_posted: str

class Ad(BaseModel):
    title: str
    description: str
    price: int
    date_posted: str    

class AdUpdate(BaseModel):
    title: str
    description: str
    price: int
    date_posted: str
    