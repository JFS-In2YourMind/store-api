from app.db.client import product_collection
from app.models.product import Product
from bson.objectid import ObjectId

async def create_product(product: Product):
    new_product = product.dict()
    result = await product_collection.insert_one(new_product)
    return {**new_product, "id": str(result.inserted_id)}

async def list_products():
    products = []
    async for doc in product_collection.find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        products.append(doc)
    return products
