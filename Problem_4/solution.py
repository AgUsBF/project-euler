def reverse_number(number):
    '''Reverse the order or numbers'''
    
    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            inverse = 0
    
            # Reverse the number
            while number != 0:
                inverse *= 10 
                inverse += number % 10
                number //= 10
    
            return inverse
    
        else:
            raise ValueError("The number must be a natural!")
    
    else:
        raise TypeError("The input must be an integer!")


def is_palindrome(number):
    '''Check if the number is a palindrome'''

    return number == reverse_number(number)


def solution(n_digits):
    '''Solution 4: Find the largest palindrome made from the product of two
    n_digits digit numbers'''

    # Check for a positive integer input
    if type(n_digits) == int:
        if n_digits > 0:
            palindrome_num = 0
            num1 = 10**n_digits - 1

            while num1 > 10**(n_digits - 1):
                num2 = 10**n_digits - 1

                while num2 > 10**(n_digits - 1):
                    number = num1 * num2

                    if is_palindrome(number):
                        if number > palindrome_num:
                            palindrome_num = number
                    
                    num2 -= 1
                
                num1 -= 1

            return palindrome_num

        else:
            raise ValueError("The number must be a natural!")

    else:
        raise TypeError("The input must be an integer!")
