class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r}, quantity={self.quantity!r})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)

    def total_cost(self) -> float:
        return self.price * self.quantity

p1 = Product("Laptop", 4500.0, 2)
print(p1)                  # Product(name='Laptop', price=4500.0, quantity=2)
print(p1.total_cost())     # 9000.0




from dataclasses import dataclass

@dataclass
class ProductDataclass:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

p2 = ProductDataclass("Laptop", 4500.0, 2)
print(p2)                  # Product(name='Laptop', price=4500.0, quantity=2)
print(p2.total_cost())     # 9000.0

