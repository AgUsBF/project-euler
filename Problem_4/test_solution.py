import unittest
from solution import reverse_number, is_palindrome, solution

class TestSolution(unittest.TestCase):
    def test_reverse_number_testcase(self):
        # Test Euler test case
        self.assertEqual(reverse_number(20), 2)
        self.assertEqual(reverse_number(302), 203)
        self.assertEqual(reverse_number(404), 404)
        self.assertEqual(reverse_number(9001), 1009)
    
    def test_reverse_number_values(self):
        # Test value error
        self.assertRaises(ValueError, reverse_number, -2)

    def test_reverse_number_type(self):
        # Test input value error
        self.assertRaises(TypeError, reverse_number, 2j)
        self.assertRaises(TypeError, reverse_number, True)
        self.assertRaises(TypeError, reverse_number, "10")
    
    def test_is_palindrome_testcase(self):
        # Test Euler test case
        self.assertEqual(is_palindrome(20), False)
        self.assertEqual(is_palindrome(302), False)
        self.assertEqual(is_palindrome(404), True)
        self.assertEqual(is_palindrome(9001), False)
        self.assertEqual(is_palindrome(9009), True)
    
    def test_is_palindrome_values(self):
        # Test value error
        self.assertRaises(ValueError, is_palindrome, -2)

    def test_is_palindrome_type(self):
        # Test input value error
        self.assertRaises(TypeError, is_palindrome, 2j)
        self.assertRaises(TypeError, is_palindrome, True)
        self.assertRaises(TypeError, is_palindrome, "10")

    def test_solution_testcase(self):
        # Test Euler test case
        self.assertEqual(solution(2), 9009)
    
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
