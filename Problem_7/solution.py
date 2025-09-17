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


def solution(nth):
    '''Solution 7: Get the n-th prime number'''

    # Check for a positive integer input
    if type(nth) == int:
        if (nth > 0):
            counter = 0
            number = 0
            
            # Check numbers until the counter equals the value of nth
            while counter < nth:
                number += 1
                
                if is_prime(number):
                    counter +=1
            
            return number
        
        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")
