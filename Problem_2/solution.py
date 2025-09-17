def solution(max_summation):
    '''Solution 2: Find the sum of the even-valued terms of the Fibonacci
    sequence whose values do not exceed max_summation'''

    # Check for a positive integer input
    if type(max_summation) == int:
        if max_summation > 0:
            term1 = 1
            term2 = 2
            summation = term2
            aux = term1 + term2

            while aux <= max_summation:
                # Reasign terms
                term1 = term2
                term2 = aux
                
                # Summ even terms
                if aux % 2 == 0:
                    summation += aux
                
                # Get next term
                aux = term1 + term2

            return summation
        
        else:
            raise ValueError("The number must be a natural!")
        
    else:
        raise TypeError("The input must be an integer!")
    