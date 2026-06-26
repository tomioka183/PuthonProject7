import sys
import os
import pytest

# Добавляем корневую директорию проекта в sys.path, чтобы 'src' был виден
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product import Product
from src.category import Category

def test_product_init_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Смартфон", "Флагман", 100000.0, 0)

def test_category_average_price():
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 10)
    category = Category("Электроника", "Гаджеты", [p1, p2])
    assert category.average_price() == 150.0

def test_category_average_price_empty():
    category = Category("Пустая категория", "Нет товаров", [])
    assert category.average_price() == 0
