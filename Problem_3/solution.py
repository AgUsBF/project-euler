def is_prime(number):
    '''Checks if the number is prime'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            # Case number = 1
            if number < 2:

                return False
            
            # Case number = 2 or 3
            elif number < 4:
            
                return True
            
            # Case number > 3: Test if it has a divisor
            else:
                for i in range(2, number // 2 + 1):
                    if number % i == 0:

                        return False
                    
                return True
            
        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")


def next_prime(number):
    '''Returns the next prime.'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:

            # Search for a prime
            while not is_prime(number + 1):
                number += 1
            
            return number + 1
        
        else:
            raise ValueError("The number must be a natural!")
    
    else:
        raise TypeError("The input must be an integer!")


def div_prime(number, prime_divider):
    '''Returns the remainder after evenly dividing
    the number all the possible times'''

    # Check for positives integer input
    if type(number) == int and type(prime_divider) == int:
        if number > 0 and prime_divider > 0:
            if is_prime(prime_divider):
                while number % prime_divider == 0:
                    number //= prime_divider

                return number

            else:
                raise ValueError("The prime divider must be a prime number!")

        else:
            raise ValueError("The number must be a natural!")

    else:
        raise TypeError("The input must be an integer!")


def solution(number):
    '''Solution 3: Get the largest prime factor of the number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 1:                
            if is_prime(number):

                return number
            
            else:
                div = 2

            while True:
                if number % div == 0:
                    number = div_prime(number, div)
                    
                    if is_prime(number):
                    
                        return number
                    
                    elif number == 1:
                    
                        return div
                    
                div = next_prime(div)

        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")
