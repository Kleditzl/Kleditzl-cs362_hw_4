import unittest
import name

class TestName(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name.combine("Logan", "Kleditz"), "Logan Kleditz")
        self.assertEqual(name.combine("", ""), " ")
        self.assertEqual(name.combine("Logan", ""), "Logan ")

if __name__ == '__main__':
    unittest.main()