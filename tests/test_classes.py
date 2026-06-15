import pytest
from src.classes import Product, Category, Smartphone, LawnGrass, BaseProduct

@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "Смартфон", 100000.0, 5)

@pytest.fixture
def smartphone_iphone():
    return Smartphone("Iphone 15", "Apple", 120000.0, 3, 3.2, "15 Pro", 256, "Titanium")

@pytest.fixture
def grass_lawn():
    return LawnGrass("Газонная трава", "Зеленая", 500.0, 10, "Россия", "14 дней", "Зеленый")


def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23"
    assert product_samsung.price == 100000.0


def test_print_mixin_product(capsys):
    Product("Samsung", "Smartphone", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Product" in captured.out
    assert "Samsung" in captured.out


def test_print_mixin_smartphone(capsys):
    Smartphone("Iphone 15", "Apple", 120000.0, 3, 3.2, "15 Pro", 256, "Titanium")
    captured = capsys.readouterr()
    assert "Smartphone" in captured.out
    assert "120000.0" in captured.out


def test_print_mixin_lawngrass(capsys):
    LawnGrass("Трава", "Газон", 100.0, 10, "РФ", "7 дней", "Зеленый")
    captured = capsys.readouterr()
    assert "LawnGrass" in captured.out


def test_base_product_abstract_error():
    with pytest.raises(TypeError):
        BaseProduct()


def test_category_init(product_samsung):
    category = Category("Электроника", "Техника", [product_samsung])
    assert category.name == "Электроника"
    assert category.products == "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт."

def test_add_product_to_category_error():
    category = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")

def test_products_add_different_class_error(smartphone_iphone, grass_lawn):
    with pytest.raises(TypeError):
        _ = smartphone_iphone + grass_lawn

def test_product_price_setter_invalid(product_samsung, capsys):
    product_samsung.price = -10.0
    assert product_samsung.price == 100000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
