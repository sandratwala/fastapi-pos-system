from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate, UserUpdate


def list_users(db: Session):
    return user_repository.get_all(db)


def get_user(db: Session, user_id: int):
    user = user_repository.get(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def create_user(db: Session, data: UserCreate):
    if user_repository.get_by_username(db, data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken",
        )
    payload = {
        "username": data.username,
        "hashed_password": hash_password(data.password),
        "role": data.role,
        "email": data.email,
    }
    return user_repository.create(db, payload)


def update_user(db: Session, user_id: int, data: UserUpdate):
    user = get_user(db, user_id)
    fields = data.model_dump(exclude_unset=True)

    if "password" in fields:
        raw_password = fields.pop("password")
        fields["hashed_password"] = hash_password(raw_password)

    return user_repository.update(db, user, fields)


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    user_repository.delete(db, user)