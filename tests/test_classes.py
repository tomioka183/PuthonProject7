import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product_1():
    return Product("Монитор", "Игровой монитор 27 дюймов", 25000.0, 10)


@pytest.fixture
def sample_product_2():
    return Product("Мышь", "Беспроводная игровая мышь", 3000.0, 50)


@pytest.fixture
def sample_category(sample_product_1, sample_product_2):
    return Category("Электроника", "Все для компьютера", [sample_product_1, sample_product_2])


@pytest.fixture
def another_category():
    return Category("Одежда", "Верхняя одежда", [Product("Куртка", "Зимняя куртка", 10000.0, 20)])


# --- Тесты для класса Product ---
def test_product_init(sample_product_1):
    """Проверяет корректность инициализации объекта Product."""
    assert sample_product_1.name == "Монитор"
    assert sample_product_1.description == "Игровой монитор 27 дюймов"
    assert sample_product_1.price == 25000.0
    assert sample_product_1.quantity == 10


# --- Тесты для класса Category ---
def test_category_init(sample_category, sample_product_1, sample_product_2):
    """Проверяет корректность инициализации объекта Category."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Все для компьютера"
    assert sample_category.products == [sample_product_1, sample_product_2]


def test_category_count(sample_category, another_category):
    """Проверяет подсчет количества категорий."""
    # Было создано две категории в рамках одного теста
    assert Category.category_count == 2


def test_product_count_in_categories(sample_category, another_category):
    """Проверяет подсчет общего количества продуктов во всех категориях."""
    # В первой категории 2 продукта, во второй категории 1 продукт. Всего 3.
    assert Category.product_count == 3
