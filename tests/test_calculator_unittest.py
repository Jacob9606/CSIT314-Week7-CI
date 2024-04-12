import unittest
import random
from calculator import add, subtract, multiply, divide

NUM_TESTS = 20

class TestCalculator(unittest.TestCase) :
    def test_add (self) :
        for _ in range (NUM_TESTS) :
            x = random. uniform(-1000, 1000)
            y = random. uniform(-1000, 1000)
            self.assertAlmostEqual (add (x, y) , x + y)

if __name__ == '__main__':
    unittest.main()


    # def test_subtract(self):
    #     self.assertEqual(subtract(10, 5), 5)
    #     self.assertEqual(subtract(-1, 1), -2)
    #     self.assertEqual(subtract(0, 0), 0)
    #     self.assertEqual(subtract(100, 50), 50)
    #
    # def test_multiply(self):
    #     self.assertEqual(multiply(3, 7), 21)
    #     self.assertEqual(multiply(-1, 3), -3)
    #     self.assertEqual(multiply(0, 10), 0)
    #     self.assertEqual(multiply(-1, -1), 1)
    #
    # def test_divide(self):
    #     self.assertEqual(divide(10, 2), 5)
    #     self.assertEqual(divide(5, 2), 2.5)
    #     self.assertEqual(divide(-1, 1), -1)
    #     self.assertEqual(divide(0, 1), 0)
    #     # 0으로 나누는 경우의 예외 처리를 테스트합니다.
    #     with self.assertRaises(ValueError):
    #         divide(10, 0)


