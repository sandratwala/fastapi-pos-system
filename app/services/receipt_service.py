from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.receipt_repository import receipt_repository
from app.repositories.sale_repository import sale_repository
from app.schemas.receipt import ReceiptCreate


def list_receipts(db: Session):
    return receipt_repository.get_all(db)


def get_receipt(db: Session, receipt_id: int):
    receipt = receipt_repository.get(db, receipt_id)
    if not receipt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receipt not found")
    return receipt


def create_receipt(db: Session, data: ReceiptCreate):
    if not sale_repository.get(db, data.sale_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sale with id {data.sale_id} does not exist",
        )
    if receipt_repository.get_by_sale(db, data.sale_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Sale {data.sale_id} already has a receipt",
        )
    return receipt_repository.create(db, data.model_dump())


def delete_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)
    receipt_repository.delete(db, receipt)