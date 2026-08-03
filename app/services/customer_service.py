from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.customer_repository import customer_repository
from app.schemas.customer import CustomerCreate, CustomerUpdate


def list_customers(db: Session):
    return customer_repository.get_all(db)

def get_customer(db: Session, customer_id: int):
    customer = customer_repository.get(db, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

def create_customer(db: Session, data: CustomerCreate):
    if customer_repository.get_by_email(db, data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A customer with this email already exists",
        )
    return customer_repository.create(db, data.model_dump())

def update_customer(db: Session, customer_id: int, data: CustomerUpdate):
    customer = get_customer(db, customer_id)
    return customer_repository.update(db, customer, data.model_dump(exclude_unset=True))

def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    customer_repository.delete(db, customer)