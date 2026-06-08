import pytest
from src.classes import Product, Category

@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "Смартфон", 100000.0, 5)

@pytest.fixture
def category_electronics(product_samsung):
    return Category("Электроника", "Техника", [product_samsung])

def test_product_init(product_samsung):
    """Тест инициализации продукта"""
    assert product_samsung.name == "Samsung Galaxy S23"
    assert product_samsung.description == "Смартфон"
    assert product_samsung.price == 100000.0
    assert product_samsung.quantity == 5

def test_category_init(category_electronics, product_samsung):
    """Тест инициализации категории"""
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Техника"
    assert category_electronics.products == "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт."

def test_category_counts():
    """Тест подсчета категорий и продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    prod1 = Product("Товар 1", "Описание 1", 100.0, 10)
    prod2 = Product("Товар 2", "Описание 2", 200.0, 5)

    cat1 = Category("Категория 1", "Описание 1", [prod1])
    assert Category.category_count == 1
    assert Category.product_count == 1

    cat2 = Category("Категория 2", "Описание 2", [prod2])
    assert Category.category_count == 2
    assert Category.product_count == 2

def test_add_product(category_electronics):
    """Тест добавления продукта в категорию"""
    Category.product_count = 1
    new_prod = Product("Iphone 15", "Смартфон от Apple", 120000.0, 3)
    category_electronics.add_product(new_prod)
    assert category_electronics.products == (
        "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 120000.0 руб. Остаток: 3 шт."
    )
    assert Category.product_count == 2

def test_new_product_classmethod():
    """Тест создания продукта через класс-метод"""
    data = {
        "name": "Nokia 3310",
        "description": "Легенда",
        "price": 3000.0,
        "quantity": 100
    }
    prod = Product.new_product(data)
    assert prod.name == "Nokia 3310"
    assert prod.description == "Легенда"
    assert prod.price == 3000.0
    assert prod.quantity == 100

def test_product_price_setter(product_samsung):
    """Тест успешного изменения цены"""
    product_samsung.price = 90000.0
    assert product_samsung.price == 90000.0

def test_product_price_setter_invalid(product_samsung, capsys):
    """Тест попытки установить некорректную цену (<= 0)"""
    product_samsung.price = -100.0
    assert product_samsung.price == 100000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

