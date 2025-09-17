import unittest
from solution import is_prime, get_prime_list, get_not_prime_list, get_prime_decomposition, solution

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

    def test_get_prime_list_testcase(self):
        # Test cases
        self.assertEqual(get_prime_list(1), [])
        self.assertEqual(get_prime_list(4), [2, 3])
        self.assertEqual(get_prime_list(10), [2, 3, 5, 7])
        self.assertEqual(get_prime_list(15), [2, 3, 5, 7, 11, 13])
    
    def test_get_prime_list_values(self):
        # Test value error
        self.assertRaises(ValueError, get_prime_list, -2)

    def test_get_prime_list_type(self):
        # Test input value error
        self.assertRaises(TypeError, get_prime_list, 2j)
        self.assertRaises(TypeError, get_prime_list, True)
        self.assertRaises(TypeError, get_prime_list, "10")

    def test_get_not_prime_list_testcase(self):
        # Test cases
        self.assertEqual(get_not_prime_list(1), [])
        self.assertEqual(get_not_prime_list(4), [4])
        self.assertEqual(get_not_prime_list(10), [4, 6, 8, 9, 10])
        self.assertEqual(get_not_prime_list(15), [4, 6, 8, 9, 10, 12, 14, 15])
    
    def test_get_not_prime_list_values(self):
        # Test value error
        self.assertRaises(ValueError, get_not_prime_list, -2)

    def test_get_not_prime_list_type(self):
        # Test input value error
        self.assertRaises(TypeError, get_not_prime_list, 2j)
        self.assertRaises(TypeError, get_not_prime_list, True)
        self.assertRaises(TypeError, get_not_prime_list, "10")
    
    def test_get_prime_decomposition_testcase(self):
        # Test cases
        self.assertEqual(get_prime_decomposition(1), ([], []))
        self.assertEqual(get_prime_decomposition(4), ([2, 3], [2, 0]))
        self.assertEqual(get_prime_decomposition(10), ([2, 3, 5, 7], [1, 0, 1, 0]))
        self.assertEqual(get_prime_decomposition(15), ([2, 3, 5, 7, 11, 13], [0, 1, 1, 0, 0, 0]))

    def test_get_prime_decomposition_values(self):
        # Test value error
        self.assertRaises(ValueError, get_prime_decomposition, -2)

    def test_get_prime_decomposition_type(self):
        # Test input value error
        self.assertRaises(TypeError, get_prime_decomposition, 2j)
        self.assertRaises(TypeError, get_prime_decomposition, True)
        self.assertRaises(TypeError, get_prime_decomposition, "10")

    def test_solution_testcase(self):
        # Test cases
        self.assertEqual(solution(3), 6)
        self.assertEqual(solution(10), 2520)

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
