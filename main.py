from src.product import Product
from src.category import Category

if __name__ == "__main__":
    print("--- Проверка Задания 1 (Исключение при количестве = 0) ---")
    try:
        bad_product = Product("Бракованный телефон", "Сломан", 15000.0, 0)
    except ValueError as e:
        print(f"Успешно поймали ошибку: {e}")

    print("\n--- Проверка Задания 2 (Средний ценник категории) ---")
    p1 = Product("Samsung Galaxy", "Смартфон", 50000.0, 5)
    p2 = Product("Iphone 15", "Флагман", 100000.0, 10)

    electronics = Category("Электроника", "Гаджеты", [p1, p2])
    print(f"Средняя цена товаров в категории '{electronics.name}': {electronics.average_price()} руб.")

    empty_category = Category("Пустая категория", "Нет товаров")
    print(f"Средняя цена в пустой категории '{empty_category.name}': {empty_category.average_price()} руб.")