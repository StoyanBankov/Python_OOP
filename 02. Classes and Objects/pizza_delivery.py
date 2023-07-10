class PizzaDelivery:

    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += price_per_quantity*quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_quantity*quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                if self.ingredients[ingredient] < quantity:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_quantity*quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with" \
               f" {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} " \
               f"and the price will be {self.price}lv."
