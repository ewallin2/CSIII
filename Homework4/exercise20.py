import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, item):
        return self.menu[item]

    def add_item(self, item, price):
        if item not in self.menu:
            self.menu[item] = price




class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.coffee_menu.get_price('espresso'), 2.50)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.coffee_menu.get_price('mocha')

    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 3.50)
        self.assertEqual(self.coffee_menu.get_price('mocha'), 3.50)

    def test_add_existing_item(self):
        result = self.coffee_menu.add_item('latte', 3.00)
        self.assertFalse(result)
        self.assertEqual(self.coffee_menu.get_price('latte'), 2.75)

if __name__ == '__main__':
    unittest.main()



