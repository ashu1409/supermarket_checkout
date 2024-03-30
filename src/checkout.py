from .item import Item

class Checkout:
    def __init__(self):
        self.cart = {}
        self.items = {
            'A': Item('A', 50, {'3_for_130': (3, 130)}),
            'B': Item('B', 30, {'2_for_45': (2, 45)}),
            'C': Item('C', 20),
            'D': Item('D', 15)
            # Add more items as needed
        }

    def scan(self, item):
        if item not in self.items:
            raise ValueError("Invalid item")
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            if item in self.items:
                item_obj = self.items[item]
                if item_obj.special_offer:
                    for offer, (quantity_req, offer_price) in item_obj.special_offer.items():
                        while quantity >= quantity_req:
                            total += offer_price
                            quantity -= quantity_req
                total += quantity * item_obj.price
        return total
