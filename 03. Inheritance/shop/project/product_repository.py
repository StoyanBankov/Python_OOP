from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, name: str):
        res = [p for p in self.products if p.name == name]
        if res:
            return res[0]

    def remove(self, name):
        product = self.find(name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        for p in self.products:
            return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
