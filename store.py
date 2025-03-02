# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет
# свои особенности, но также существуют общие характеристики, такие как
# адрес, название и ассортимент товаров.
# Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
#
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
#
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

# Создаем три магазина
store1 = Store("'Фрукты'", "ул. Ленина, 10")
store2 = Store("'Мясо'", "ул. Мира, 5")
store3 = Store("'Молоко'", "ул. Пушкина, 15")

# Добавляем товары в каждый магазин
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("баранина", 600)
store2.add_item("свинина", 450)

store3.add_item("молоко", 100)
store3.add_item("сыр", 1200)
store3.add_item("сметана", 80)


# магазины:
print(f"Магазин: {store1.name}, Адрес: {store1.address}")
print("Текущий ассортимент:", store1.items)
print(f"Магазин: {store2.name}, Адрес: {store2.address}")
print("Текущий ассортимент:", store2.items)

# Тестируем методы на магазине молоко
print(f"Магазин: {store3.name}, Адрес: {store3.address}")
print("Текущий ассортимент:", store3.items)
# Добавляем новый товар
store3.add_item("кефир", 90)
print("После добавления кефира:", store3.items)

# Обновляем цену товара
store3.update_price("бобер", 1500)

store3.update_price("сыр", 1500)
print("После обновления цены apples:", store3.items)

# Получаем цену баранины из разных магазинов
price = store1.get_price("баранина")
print(f"Цена баранины: {price}")
price = store2.get_price("баранина")
print(f"Цена баранины: {price}")

# Удаляем товар
store3.remove_item("молоко")
print("После удаления молока:", store3.items)

# Пытаемся получить цену удаленного товара
price = store3.get_price("молоко")
print(f"Цена молока после удаления: {price}")