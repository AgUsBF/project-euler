import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(2), 81)
        self.assertEqual(solution(3), 81*8)
    
    def test_solution_values(self):
        # Test value error
        self.assertRaises(ValueError, solution, -1)
        self.assertRaises(ValueError, solution, 0)

    def test_solution_type(self):
        # Test input value error
        self.assertRaises(TypeError, solution, 2j)
        self.assertRaises(TypeError, solution, "10")
        self.assertRaises(TypeError, solution, True)

if __name__ == "__main__":
    unittest.main()
