import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1, 4, 4, 4, 0, 4, 3, 3, 1]), [1, 12, 0, 4, 6, 1])

    def test_2(self):
        self.assertEqual(solution([1, 1, 7, 7, 3]), [2, 14, 3])

    def test_3(self):
        self.assertEqual(solution([1, 1, 1, 1, 1]), [5])

    def test_4(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]), [5, 10])

    def test_5(self):
        self.assertEqual(solution([]), [])

    def test_6(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()