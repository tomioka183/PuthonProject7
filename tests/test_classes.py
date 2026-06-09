import pytest
from src.classes import Product, Category

@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "Смартфон", 100000.0, 5)

@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "Смартфон от Apple", 120000.0, 3)

@pytest.fixture
def category_electronics(product_samsung):
    return Category("Электроника", "Техника", [product_samsung])

def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23"
    assert product_samsung.description == "Смартфон"
    assert product_samsung.price == 100000.0
    assert product_samsung.quantity == 5

def test_product_str(product_samsung):
    assert str(product_samsung) == "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт."

def test_category_str(category_electronics, product_iphone):
    assert str(category_electronics) == "Электроника, количество продуктов: 5 шт."

    category_electronics.add_product(product_iphone)
    assert str(category_electronics) == "Электроника, количество продуктов: 8 шт."

def test_products_add(product_samsung, product_iphone):
    assert product_samsung + product_iphone == 860000.0


def test_category_products_getter(category_electronics, product_iphone):
    category_electronics.add_product(product_iphone)
    assert category_electronics.products == (
        "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 120000.0 руб. Остаток: 3 шт."
    )

def test_new_product_classmethod():
    data = {
        "name": "Nokia 3310",
        "description": "Легенда",
        "price": 3000.0,
        "quantity": 100
    }
    prod = Product.new_product(data)
    assert prod.name == "Nokia 3310"
    assert prod.price == 3000.0

def test_product_price_setter(product_samsung):
    product_samsung.price = 90000.0
    assert product_samsung.price == 90000.0

def test_product_price_setter_invalid(product_samsung, capsys):
    product_samsung.price = -100.0
    assert product_samsung.price == 100000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
