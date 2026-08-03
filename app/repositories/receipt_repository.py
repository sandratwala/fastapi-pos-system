from app.models.receipt import Receipt
from sqlalchemy.orm import Session


class ReceiptRepository:
    def __init__(self):
        self.model = Receipt

    def get(self, db: Session, id: int):
        return db.get(self.model, id)

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_by_sale(self, db: Session, sale_id: int):
        return db.query(self.model).filter(self.model.sale_id == sale_id).first()

    def create(self, db: Session, data: dict):
        receipt = self.model(**data)
        db.add(receipt)
        db.commit()
        db.refresh(receipt)
        return receipt

    def delete(self, db: Session, db_obj: Receipt):
        db.delete(db_obj)
        db.commit()


receipt_repository = ReceiptRepository()