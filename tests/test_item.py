import unittest
from supermarket_checkout.src.item import Item

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item("A", 50, {'3_for_130': (3, 130)})
        self.assertEqual(item.name, "A")
        self.assertEqual(item.price, 50)
        self.assertEqual(item.special_offer, {'3_for_130': (3, 130)})

if __name__ == '__main__':
    unittest.main()
