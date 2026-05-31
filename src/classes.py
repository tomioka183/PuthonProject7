class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
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
    def price(self, new_price):
        """Сеттер для цены с проверкой (Задание 4)."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    """Класс для представления категории товаров."""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product):
        """Метод для добавления товара в приватный список (Задание 1)."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров в нужном формате (Задание 2)."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str