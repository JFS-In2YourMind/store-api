from fastapi import APIRouter
from app.models.product import Product
from app.services.product_service import create_product, list_products

router = APIRouter()

@router.post("/", response_model=dict)
async def add_product(product: Product):
    return await create_product(product)

@router.get("/", response_model=list)
async def get_products():
    return await list_products()
