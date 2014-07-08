import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def testDiscountCorrect(self):
        price = calculate_discount(100,.1,.1)

        self.assertEqual(price,81)

    def testZeroDiscount(self):
        price = calculate_discount(100,0,.1)

        self.assertEqual(price,90)

    def testZeroDiscount2(self):
        price = calculate_discount(100,.1,0)

        self.assertEqual(price,90)

    def testpriceNotNegative(self):
        price = calculate_discount(100,1.5,5.)

        self.assertGreater(price,0)

    def testpriceNotBigger(self):
    	initial_price = 100.
        price = calculate_discount(initial_price,1.5,5.)

        self.assertGreater(price,initial_price)

if __name__ == '__main__':
	unittest.main()