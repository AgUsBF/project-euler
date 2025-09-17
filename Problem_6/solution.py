def sum_squares(number):
    '''Calculate the sum of the squeared numbers from 1 up to number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            result = 0
            
            # Add the squared numbers
            for i in range(1, number + 1):
                result += i**2
            
            return result
        
        else:
            raise ValueError("The number must be a natural!")

    else:
        raise TypeError("The input must be an integer!")


def squared_sum(number):
    '''Calculate the squared of th sum of numbers from 1 up to number'''

    # Check for a positive integer input
    if (type(number) == int):
        if (number > 0):
            result = 0

            # Add the numbers, then squared the result
            for i in range(1, number + 1):
                result += i

            return result**2

        else:
            raise ValueError("The number must be a natural!")

    else:
        raise TypeError("The input must be an integer!")


def solution(num):
    '''Solution 6: Calculate the difference between the squared sum adn the 
    sum of the squared numbers'''
    
    return squared_sum(num) - sum_squares(num)
