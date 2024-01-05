from sqlalchemy.orm import Session
import models
from models import User
from models import Ad 
from schemas import UserCreate, UserUpdate, AdCreate, AdUpdate

def create_user(db: Session, user: models.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def update_user(db: Session, user_id: int, user: models.UserUpdate):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def create_ad(db: Session, ad: models.AdCreate):
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def get_ad(db: Session, ad_id: int):
    return db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()

def update_ad(db: Session, ad_id: int, ad: models.AdUpdate):
    db_ad = db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()
    for key, value in ad.dict().items():
        setattr(db_ad, key, value)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def delete_ad(db: Session, ad_id: int):
    db_ad = db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()
    db.delete(db_ad)
    db.commit()
    return db_ad
