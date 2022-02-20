from errors import ItemAlreadyExistsError, ItemNotExistError
from item import Item


class ShoppingCart:
    """Initializing the shopping cart to an empty array"""
    def __init__(self):
        self.cart = []

    """Adds item to the shopping cart"""
    def add_item(self, item: Item):
        # Checks if the item already exists in the shopping cart
        if item not in self.cart:
            self.cart.append(item)
        else:
            raise ItemAlreadyExistsError

    pass

    """Removes item from the shopping cart"""
    def remove_item(self, item_name: str):
        # Search in the shopping cart for the item
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                return
        raise ItemNotExistError

    pass

    """Calculate the subtotal cost of all the item in the shopping cart"""
    def get_subtotal(self) -> int:
        subtotal = 0
        # Iterating over the shopping cart and summing each item price
        for item in self.cart:
            subtotal += item.price
        return subtotal

    pass
