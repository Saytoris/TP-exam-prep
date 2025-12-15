import unittest
from logic import calculate_sum

class TestExtendedProgression(unittest.TestCase):

    def test_type_check(self):
        """
        Перевіряємо, чи повертає функція об'єкт правильного типу.
        Використовуємо assertIsInstance з першого скріншоту.
        """
        result = calculate_sum(5)
        # Переконуємося, що результат — це ціле число (int), а не float чи рядок
        self.assertIsInstance(result, int) 
        # Переконуємося, що результат не є None (з другого скріншоту)
        self.assertIsNotNone(result)

    def test_value_bounds(self):
        """
        Перевіряємо математичні межі результату.
        Використовуємо assertGreater та assertLess з третього скріншоту.
        """
        n = 10
        result = calculate_sum(n)  # Очікується 110
        
        # Сума додатних чисел має бути більшою за 0
        self.assertGreater(result, 0)
        
        # Сума (110) має бути більшою за саме n (10)
        self.assertGreater(result, n)
        
        # Для n=10 сума точно менша за 200
        self.assertLess(result, 200)

    def test_logic_properties(self):
        """
        Перевіряємо властивості чисел через булеві вирази.
        Використовуємо assertTrue та assertFalse з другого скріншоту.
        """
        result = calculate_sum(4)  # 2 + 4 + 6 + 8 = 20
        
        # Перевіряємо, чи результат є парним числом (сума парних завжди парна)
        is_even = (result % 2 == 0)
        self.assertTrue(is_even, "Результат має бути парним числом")
        
        # Перевіряємо, що результат НЕ є непарним
        self.assertFalse(result % 2 != 0)

    def test_membership(self):
        """
        Перевіряємо, чи входить результат у набір очікуваних значень.
        Використовуємо assertIn з другого скріншоту.
        """
        # Обчислюємо для n=3 (2+4+6 = 12)
        result = calculate_sum(3)
        
        # Припустимо, ми знаємо "магічні числа" для перших кроків
        known_results = [2, 6, 12, 20, 30]
        
        # Перевіряємо, що 12 є в цьому списку
        self.assertIn(result, known_results)

    def test_inequality(self):
        """
        Перевіряємо, що результат НЕ дорівнює певному значенню.
        """
        result = calculate_sum(5) # 30
        # Результат точно не повинен дорівнювати 0 для n=5
        self.assertNotEqual(result, 0)

if __name__ == '__main__':
    unittest.main()