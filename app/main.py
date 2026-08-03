from fastapi import FastAPI

from app.database import Base, engine
from app.routers.category_router import router as category_router
from app.routers.supplier_router import router as supplier_router
from app.routers.product_router import router as product_router
from app.routers.customer_router import router as customer_router
from app.routers.user_router import router as user_router
from app.routers.sale_router import router as sale_router
from app.routers.sale_item_router import router as sale_item_router
from app.routers.payment_router import router as payment_router
from app.routers.receipt_router import router as receipt_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sandie's POS API", version="1")

app.include_router(category_router)
app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(customer_router)
app.include_router(user_router)
app.include_router(sale_router)
app.include_router(sale_item_router)
app.include_router(payment_router)
app.include_router(receipt_router)