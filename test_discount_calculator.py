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

    def testAbs100_Percent(self):
        price = calculate_discount(100,0,1)

        self.assertEqual(price,0)

    def testRel100_Percent(self):
        price = calculate_discount(100,1,0)

        self.assertEqual(price,0)

    def testPercAbove100(self):
    	with self.assertRaises(ValueError):
	        price = calculate_discount(100,1.5,5.)

    
if __name__ == '__main__':
	unittest.main()