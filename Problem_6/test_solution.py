import unittest
from solution import sum_squares, squared_sum, solution

class TestSolution(unittest.TestCase):
    def test_sum_squares_testcase(self):
        # Test cases
        self.assertEqual(sum_squares(1), 1)
        self.assertEqual(sum_squares(2), 5)
        self.assertEqual(sum_squares(3), 14)
        self.assertEqual(sum_squares(4), 30)
        self.assertEqual(sum_squares(5), 55)
    
    def test_sum_squares_values(self):
        # Test value error
        self.assertRaises(ValueError, sum_squares, -2)

    def test_sum_squares_type(self):
        # Test input value error
        self.assertRaises(TypeError, sum_squares, 2j)
        self.assertRaises(TypeError, sum_squares, True)
        self.assertRaises(TypeError, sum_squares, "10")

    def test_squared_sum_testcase(self):
        # Test cases
        self.assertEqual(squared_sum(1), 1)
        self.assertEqual(squared_sum(2), 9)
        self.assertEqual(squared_sum(3), 36)
        self.assertEqual(squared_sum(4), 100)
        self.assertEqual(squared_sum(5), 15**2)
    
    def test_squared_sum_values(self):
        # Test value error
        self.assertRaises(ValueError, squared_sum, -2)

    def test_squared_sum_type(self):
        # Test input value error
        self.assertRaises(TypeError, squared_sum, 2j)
        self.assertRaises(TypeError, squared_sum, True)
        self.assertRaises(TypeError, squared_sum, "10")

    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(2), 4)
        self.assertEqual(solution(3), 22)
        self.assertEqual(solution(4), 70)
        self.assertEqual(solution(10), 2640)
    
    def test_solution_values(self):
        # Test value error
        self.assertRaises(ValueError, solution, -2)

    def test_solution_type(self):
        # Test input value error
        self.assertRaises(TypeError, solution, 2j)
        self.assertRaises(TypeError, solution, True)
        self.assertRaises(TypeError, solution, "10")

if __name__ == "__main__":
    unittest.main()
