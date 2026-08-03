from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.customer_repository import customer_repository
from app.repositories.sale_repository import sale_repository
from app.repositories.user_repository import user_repository
from app.schemas.sale import SaleCreate, SaleUpdate


def list_sales(db: Session):
    return sale_repository.get_all(db)


def get_sale(db: Session, sale_id: int):
    sale = sale_repository.get(db, sale_id)
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return sale


def _validate_references(db: Session, data: SaleCreate):
    if not user_repository.get(db, data.user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {data.user_id} does not exist",
        )

    if data.customer_id is not None and not customer_repository.get(db, data.customer_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {data.customer_id} does not exist",
        )


def create_sale(db: Session, data: SaleCreate):
    _validate_references(db, data)
    return sale_repository.create(db, data.model_dump())


def update_sale(db: Session, sale_id: int, data: SaleUpdate):
    sale = get_sale(db, sale_id)
    if data.customer_id is not None and not customer_repository.get(db, data.customer_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {data.customer_id} does not exist",
        )
    return sale_repository.update(db, sale, data.model_dump(exclude_unset=True))


def delete_sale(db: Session, sale_id: int):
    sale = get_sale(db, sale_id)
    sale_repository.delete(db, sale)