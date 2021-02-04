import unittest
import cube_calc

class TestCube(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(cube_calc.volume(2), 8)
        self.assertEqual(cube_calc.volume(-3), False)
        self.assertEqual(cube_calc.volume(2.20), 10.648000000000003)
if __name__ == '__main__':
    unittest.main()