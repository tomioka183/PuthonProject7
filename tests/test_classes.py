import pytest
from src.classes import Product, Category

def test_product_price_setter():
    prod = Product("Samsung", "Smartphone", 1000.0, 10)
    prod.price = -500
    assert prod.price == 1000.0  # Цена не изменилась
    prod.price = 1200.0
    assert prod.price == 1200.0

def test_category_products_str():
    prod = Product("Samsung", "Smartphone", 1000.0, 10)
    cat = Category("Electronics", "Gadgets")
    cat.add_product(prod)
    assert cat.products == "Samsung, 1000.0 руб. Остаток: 10 шт."

def test_new_product_classmethod():
    data = {"name": "Nokia", "description": "Old", "price": 500.0, "quantity": 1}
    prod = Product.new_product(data)
    assert prod.name == "Nokia"