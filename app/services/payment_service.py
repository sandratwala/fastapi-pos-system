from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.payment_repository import payment_repository
from app.repositories.sale_repository import sale_repository
from app.schemas.payment import PaymentCreate, PaymentUpdate


def list_payments(db: Session):
    return payment_repository.get_all(db)


def get_payment(db: Session, payment_id: int):
    payment = payment_repository.get(db, payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment


def create_payment(db: Session, data: PaymentCreate):
    if not sale_repository.get(db, data.sale_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sale with id {data.sale_id} does not exist",
        )
    return payment_repository.create(db, data.model_dump())


def update_payment(db: Session, payment_id: int, data: PaymentUpdate):
    payment = get_payment(db, payment_id)
    fields = data.model_dump(exclude_unset=True)
    return payment_repository.update(db, payment, fields)


def delete_payment(db: Session, payment_id: int):
    payment = get_payment(db, payment_id)
    payment_repository.delete(db, payment)