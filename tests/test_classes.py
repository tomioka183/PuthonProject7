import pytest
from src.classes import Product, Category, Smartphone, LawnGrass, BaseProduct, PrintMixin

@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "Смартфон", 100000.0, 5)

def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23"
    assert product_samsung.description == "Смартфон"
    assert product_samsung.price == 100000.0
    assert product_samsung.quantity == 5

def test_print_mixin(capsys):
    Product("Samsung", "Smartphone", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Product" in captured.out
    assert "Samsung" in captured.out
    assert "1000.0" in captured.out

def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct()

def test_smartphone_init_and_mixin(capsys):
    Smartphone("Iphone 15", "Apple", 120000.0, 3, 3.2, "15 Pro", 256, "Titanium")
    captured = capsys.readouterr()
    assert "Smartphone" in captured.out
    assert "120000.0" in captured.out

def test_products_add_different_class():
    prod = Product("Samsung", "Smartphone", 1000.0, 5)
    grass = LawnGrass("Трава", "Газон", 100.0, 10, "РФ", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = prod + grass

def test_add_product_to_category_incorrect():
    category = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        category.add_product("Просто строка")