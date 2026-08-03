from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"), nullable=False)
    payment_method = Column(String(50), nullable=False)
    amount_paid = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sale = relationship("Sale", back_populates="payments")