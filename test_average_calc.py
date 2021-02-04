import unittest
import average_calc

class TestAverage_Calc(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average_calc.average([5,5,5]), 5)
        self.assertEqual(average_calc.average([0,0,0]), 0)
        self.assertEqual(average_calc.average([]), 0)
if __name__ == '__main__':
    unittest.main()