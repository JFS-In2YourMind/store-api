from app.models.product import Product

def test_create_product_model():
    product = Product(name="Tênis", price=199.90)
    assert product.name == "Tênis"
    assert product.price == 199.90
    assert product.in_stock is True
