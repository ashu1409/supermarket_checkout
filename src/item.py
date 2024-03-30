class Item:
    def __init__(self, name, price, special_offer=None):
        self.name = name
        self.price = price
        self.special_offer = special_offer if special_offer else {}
      
