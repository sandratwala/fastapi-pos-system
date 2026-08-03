from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.product_repository import product_repository
from app.repositories.sale_item_repository import sale_item_repository
from app.repositories.sale_repository import sale_repository
from app.schemas.sale_item import SaleItemCreate, SaleItemUpdate


def list_sale_items(db: Session):
    return sale_item_repository.get_all(db)


def list_items_for_sale(db: Session, sale_id: int):
    _get_sale_or_404(db, sale_id)
    return sale_item_repository.get_by_sale(db, sale_id)


def get_sale_item(db: Session, sale_item_id: int):
    sale_item = sale_item_repository.get(db, sale_item_id)
    if not sale_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale item not found")
    return sale_item


def _get_sale_or_404(db: Session, sale_id: int):
    sale = sale_repository.get(db, sale_id)
    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sale with id {sale_id} does not exist",
        )
    return sale


def create_sale_item(db: Session, data: SaleItemCreate):
    _get_sale_or_404(db, data.sale_id)

    if not product_repository.get(db, data.product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {data.product_id} does not exist",
        )

    return sale_item_repository.create(db, data.model_dump())


def update_sale_item(db: Session, sale_item_id: int, data: SaleItemUpdate):
    sale_item = get_sale_item(db, sale_item_id)
    fields = data.model_dump(exclude_unset=True)
    return sale_item_repository.update(db, sale_item, fields)


def delete_sale_item(db: Session, sale_item_id: int):
    sale_item = get_sale_item(db, sale_item_id)
    sale_item_repository.delete(db, sale_item)