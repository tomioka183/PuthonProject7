class Product:
    """
    Класс для представления товара в магазине.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.
    """

    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество всех уникальных товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Автоматическое обновление счетчиков при создании категории
        Category.category_count += 1
        Category.product_count += len(products)


