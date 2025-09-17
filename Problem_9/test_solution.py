import unittest
from solution import calculate_b,calculate_c, solution

class TestSolution(unittest.TestCase):
    def test_calculate_b_testcase(self):
        # Test cases
        self.assertEqual(calculate_b(3 + 4 + 5, 3), 4)
    
    def test_calculate_c_testcase(self):
        # Test cases
        self.assertEqual(calculate_c(3, 4), 5)
    
    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(3 + 4 + 5), 3 * 4 * 5)
    
    def test_solution_values(self):
        # Test value error
        self.assertRaises(ValueError, solution, -1)
        self.assertRaises(ValueError, solution, 0)
        self.assertRaises(ValueError, solution, 13)

    def test_solution_type(self):
        # Test input value error
        self.assertRaises(TypeError, solution, 2j)
        self.assertRaises(TypeError, solution, "10")
        self.assertRaises(TypeError, solution, True)

if __name__ == "__main__":
    unittest.main()
