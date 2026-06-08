class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает товар из словаря (Задание 3)."""
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity")
        )

    @property
    def price(self):
        """Геттер для цены (Задание 4)."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой (Задание 4)."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        # Задание 1: приватный список товаров
        self.__products = products if products is not None else []

        # Подсчет количества категорий и уникальных товаров
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию (Задание 1)."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода товаров в формате строки (Задание 2)."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return result.strip()

