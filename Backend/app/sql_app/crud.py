from fastapi import HTTPException
from sqlalchemy.orm import Session
from sql_app import models
from sql_app import schemas
from sql_app.database import SessionLocal

def create_user(user: schemas.UserCreate, db: Session = SessionLocal()):
    """
    Create a new user in the database.

    Args:
        user (schemas.UserCreate): User creation data.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.User: Created user.
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db: Session = SessionLocal()):
    """
    Get a user by ID from the database.

    Args:
        user_id (int): User ID.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.User: User if found, None otherwise.
    """
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def update_user(user_id: int, user: schemas.UserUpdate, db: Session = SessionLocal()):
    """
    Update a user in the database.

    Args:
        user_id (int): User ID.
        user (schemas.UserUpdate): Updated user data.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.User: Updated user.
    """
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

def delete_user(user_id: int, db: Session = SessionLocal()):
    """
    Delete a user from the database.

    Args:
        user_id (int): User ID.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.User: Deleted user.
    """
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

def create_ad(ad: schemas.AdCreate, db: Session = SessionLocal()):
    """
    Create a new ad in the database.

    Args:
        ad (schemas.AdCreate): Ad creation data.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.Ad: Created ad.
    """
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def get_ad(ad_id: int, db: Session = SessionLocal()):
    """
    Get an ad by ID from the database.

    Args:
        ad_id (int): Ad ID.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.Ad: Ad if found, None otherwise.
    """
    return db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()

def update_ad(ad_id: int, ad: schemas.AdUpdate, db: Session = SessionLocal()):
    """
    Update an ad in the database.

    Args:
        ad_id (int): Ad ID.
        ad (schemas.AdUpdate): Updated ad data.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.Ad: Updated ad.
    """
    db_ad = db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()
    for key, value in ad.dict().items():
        setattr(db_ad, key, value)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def delete_ad(ad_id: int, db: Session = SessionLocal()):
    """
    Delete an ad from the database.

    Args:
        ad_id (int): Ad ID.
        db (Session, optional): Database session. Defaults to SessionLocal().

    Returns:
        models.Ad: Deleted ad.
    """
    db_ad = db.query(models.Ad).filter(models.Ad.ad_id == ad_id).first()
    db.delete(db_ad)
    db.commit()
    return db_ad
