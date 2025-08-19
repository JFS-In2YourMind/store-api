from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., example="Camisa")
    description: Optional[str] = Field(None, example="Camisa branca")
    price: float = Field(..., gt=0, example=59.90)
    in_stock: bool = Field(default=True)
