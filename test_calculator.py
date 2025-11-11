import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-1, 7), -7)
        self.assertEqual(calculator.multiply(0, 567), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.divide(12, 2), 6)
        self.assertAlmostEqual(calculator.divide(3, 2), 1.5, places=7)
        self.assertEqual(calculator.divide(-21, 3), -7)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13, places=7)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17, places=7)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(calculator.sqrt(25), 5)
        self.assertAlmostEqual(calculator.sqrt(2), 1.41421356, places=7)# 3 assertions
        with self.assertRaises(ValueError):
            calculator.sqrt(-3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()