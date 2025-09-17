import unittest
from solution import is_prime, next_prime, div_prime, solution

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

    def test_next_prime_testcase(self):
        # Test cases
        self.assertEqual(next_prime(1), 2)
        self.assertEqual(next_prime(2), 3)
        self.assertEqual(next_prime(3), 5)
        self.assertEqual(next_prime(5), 7)
        self.assertEqual(next_prime(7), 11)
        self.assertEqual(next_prime(11), 13)
        self.assertEqual(next_prime(13), 17)
        self.assertEqual(next_prime(17), 19)
        self.assertEqual(next_prime(19), 23)
        self.assertEqual(next_prime(23), 29)
    
    def test_next_prime_values(self):
        # Test value error
        self.assertRaises(ValueError, next_prime, -2)

    def test_next_prime_type(self):
        # Test input value error
        self.assertRaises(TypeError, next_prime, 2j)
        self.assertRaises(TypeError, next_prime, True)
        self.assertRaises(TypeError, next_prime, "10")

    def test_div_prime_testcase(self):
        # Test cases
        self.assertEqual(div_prime(2, 2), 1)
        self.assertEqual(div_prime(3, 2), 3)
        self.assertEqual(div_prime(5, 2), 5)
        self.assertEqual(div_prime(6, 2), 3)
        self.assertEqual(div_prime(5, 3), 5)
        self.assertEqual(div_prime(10, 2), 5)
        self.assertEqual(div_prime(20, 2), 5)
        self.assertEqual(div_prime(100, 2), 25)
    
    def test_div_prime_values(self):
        # Test value error
        self.assertRaises(ValueError, div_prime, -6, 2)
        self.assertRaises(ValueError, div_prime, 6, -2)
        self.assertRaises(ValueError, div_prime, 6, 4)

    def test_div_prime_type(self):
        # Test input value error
        self.assertRaises(TypeError, div_prime, 2j, 3)
        self.assertRaises(TypeError, div_prime, "10", 3)
        self.assertRaises(TypeError, div_prime, True, 3)
        self.assertRaises(TypeError, div_prime, 20, 3j)
        self.assertRaises(TypeError, div_prime, 20, "3")
        self.assertRaises(TypeError, div_prime, 20, True)

    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(2), 2)
        self.assertEqual(solution(3), 3)
        self.assertEqual(solution(4), 2)
        self.assertEqual(solution(5), 5)
        self.assertEqual(solution(6), 3)
        self.assertEqual(solution(10), 5)
        self.assertEqual(solution(20), 5)
        self.assertEqual(solution(13195), 29)
    
    def test_solution_values(self):
        # Test value error
        self.assertRaises(ValueError, solution, -1)
        self.assertRaises(ValueError, solution, 0)
        self.assertRaises(ValueError, solution, 1)

    def test_solution_type(self):
        # Test input value error
        self.assertRaises(TypeError, solution, 2j)
        self.assertRaises(TypeError, solution, "10")
        self.assertRaises(TypeError, solution, True)

if __name__ == "__main__":
    unittest.main()
