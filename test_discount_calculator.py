import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def testDiscountCorrect(self):
        price = calculate_discount(100,.1,.1)

        self.assertEqual(price,81)


if __name__ == '__main__':
	unittest.main()