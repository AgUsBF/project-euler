def calculate_b(number, a):
    '''Get the term b from a'''
        
    return (number - 2 * a) * number / (number - a) / 2
    

def calculate_c(a, b):
    '''Get the term c from a and b'''

    return (a**2 + b**2)**0.5
        

def solution(number):
    '''Solution 9: Get the product of the Pythagorean triplet that sum number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:

            for a in range(1, number // 3):
                b = calculate_b(number, a)
                c = calculate_c(a, b)

                if a == int(a) and b == int(b) and c == int(c):
                    
                    return int(a * b * c)

            raise ValueError("No Pythagorean triplet was found!")
        
        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")
    