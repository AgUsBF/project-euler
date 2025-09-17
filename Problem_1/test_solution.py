import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_testcase(self):
        # Test Euler test case
        self.assertEqual(solution(10), 23)
    
    def test_values(self):
        # Test value error
        self.assertRaises(ValueError, solution, -2)

    def test_type(self):
        # Test input value error
        self.assertRaises(TypeError, solution, 2j)
        self.assertRaises(TypeError, solution, True)
        self.assertRaises(TypeError, solution, "10")

if __name__ == "__main__":
    unittest.main()
