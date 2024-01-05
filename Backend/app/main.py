from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import crud 
from database import SessionLocal, engine
import models

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users CRUD operations
@app.post("/users/", response_model=models.User)
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=models.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)

@app.put("/users/{user_id}", response_model=models.User)
def update_user(user_id: int, user: models.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)

@app.delete("/users/{user_id}", response_model=models.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)

# Ads CRUD operations
@app.post("/ads/", response_model=models.Ad)
def create_ad(ad: models.AdCreate, db: Session = Depends(get_db)):
    return crud.create_ad(db=db, ad=ad)

@app.get("/ads/{ad_id}", response_model=models.Ad)
def read_ad(ad_id: int, db: Session = Depends(get_db)):
    return crud.get_ad(db=db, ad_id=ad_id)

@app.put("/ads/{ad_id}", response_model=models.Ad)
def update_ad(ad_id: int, ad: models.AdUpdate, db: Session = Depends(get_db)):
    return crud.update_ad(db=db, ad_id=ad_id, ad=ad)

@app.delete("/ads/{ad_id}", response_model=models.Ad)
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    return crud.delete_ad(db=db, ad_id=ad_id)

