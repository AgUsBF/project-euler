def solution (number):
    '''Solution 1: Find the sum of all the multiples of 3 or 5 below input number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            summation = 0
            
            # Search for the multiples
            for i in range(0,number):
                if (i % 3 == 0 or i % 5 == 0):
                    summation += i

            return summation
        
        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")
    