import unittest
from logic import calculate_sum

class TestProgressionSum(unittest.TestCase):
    
    def test_simple_case(self):
        # n=3 (2, 4, 6) -> сума 12
        self.assertEqual(calculate_sum(3), 12)

    def test_zero(self):
        # n=0 -> сума 0
        self.assertEqual(calculate_sum(0), 0)

    def test_large_number(self):
        # n=10 -> 10 * 11 = 110
        self.assertEqual(calculate_sum(10), 110)

    def test_negative_input(self):
        # Перевірка на викидання помилки при від'ємному числі
        with self.assertRaises(ValueError):
            calculate_sum(-5)

    def test_invalid_type(self):
        # Перевірка на викидання помилки при введенні рядка
        with self.assertRaises(TypeError):
            calculate_sum("string")

if __name__ == '__main__':
    unittest.main()