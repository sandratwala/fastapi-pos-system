from sqlalchemy import Column, Integer, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True) 
    sale_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)
    tax_amount = Column(Numeric(10, 2), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    customer = relationship("Customer", back_populates="sales")
    user = relationship("User", back_populates="sales")
    sale_items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="sale", cascade="all, delete-orphan")
    receipt = relationship("Receipt", back_populates="sale", uselist=False, cascade="all, delete-orphan")