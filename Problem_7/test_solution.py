import unittest
from solution import is_prime, solution

class TestSolution(unittest.TestCase):
    def test_is_prime_testcase(self):
        # Test cases
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(99), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(29), True)
    
    def test_is_prime_values(self):
        # Test value error
        self.assertRaises(ValueError, is_prime, -2)

    def test_is_prime_type(self):
        # Test input value error
        self.assertRaises(TypeError, is_prime, 2j)
        self.assertRaises(TypeError, is_prime, True)
        self.assertRaises(TypeError, is_prime, "10")

    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(1), 2)
        self.assertEqual(solution(2), 3)
        self.assertEqual(solution(3), 5)
        self.assertEqual(solution(4), 7)
        self.assertEqual(solution(5), 11)
        self.assertEqual(solution(6), 13)
    
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
