import pytest
from src.classes import Product, Category, Smartphone, LawnGrass

@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23", "Смартфон", 100000.0, 5)

@pytest.fixture
def phone_iphone():
    return Smartphone("Iphone 15", "Смартфон от Apple", 120000.0, 3, 3.2, "15 Pro", 256, "Titanium")

@pytest.fixture
def grass_lawn():
    return LawnGrass("Газонная трава", "Зеленая", 500.0, 10, "Россия", "14 дней", "Зеленый")

def test_smartphone_init(phone_iphone):
    """Тест инициализации смартфона"""
    assert phone_iphone.name == "Iphone 15"
    assert phone_iphone.efficiency == 3.2
    assert phone_iphone.model == "15 Pro"
    assert phone_iphone.memory == 256
    assert phone_iphone.color == "Titanium"

def test_lawngrass_init(grass_lawn):
    """Тест инициализации газонной травы"""
    assert grass_lawn.name == "Газонная трава"
    assert grass_lawn.country == "Россия"
    assert grass_lawn.germination_period == "14 дней"
    assert grass_lawn.color == "Зеленый"

def test_products_add_same_class(product_samsung):
    """Тест сложения продуктов одного класса"""
    product2 = Product("Samsung Galaxy S22", "Старый смарт", 80000.0, 2)
    # 100000 * 5 + 80000 * 2 = 500000 + 160000 = 660000
    assert product_samsung + product2 == 660000.0

def test_products_add_different_class(phone_iphone, grass_lawn):
    """Тест ошибки при сложении продуктов РАЗНЫХ классов"""
    with pytest.raises(TypeError):
        _ = phone_iphone + grass_lawn

def test_add_product_to_category_correct(phone_iphone):
    """Тест успешного добавления смартфона в категорию"""
    category = Category("Электроника", "Техника")
    category.add_product(phone_iphone)
    assert category.products == "Iphone 15, 120000.0 руб. Остаток: 3 шт."

def test_add_product_to_category_incorrect():
    """Тест ошибки при попытке добавить в категорию не-продукт (строку)"""
    category = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        category.add_product("Просто тестовая строка")

def test_product_str(product_samsung):
    assert str(product_samsung) == "Samsung Galaxy S23, 100000.0 руб. Остаток: 5 шт."