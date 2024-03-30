import unittest
from supermarket_checkout.src.checkout import Checkout

class TestCheckout(unittest.TestCase):
    def test_scan(self):
        checkout = Checkout()
        checkout.scan("A")
        self.assertEqual(checkout.cart, {"A": 1})
        checkout.scan("B")
        self.assertEqual(checkout.cart, {"A": 1, "B": 1})

    def test_calculate_total(self):
        checkout = Checkout()
        checkout.scan("A")
        checkout.scan("A")
        checkout.scan("A")
        total = checkout.calculate_total()
        self.assertEqual(total, 130)

if __name__ == '__main__':
    unittest.main()
  
