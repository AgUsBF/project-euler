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


def get_prime_list(number):
    '''Get the list of the prime numbers up to the input number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            primes = []

            # Test if numbers are prime and add them to the prime list
            for i in range(2, number + 1):
                if (is_prime(i)):
                    primes.append(i)

            return primes

        else:
            raise ValueError("The number must be a natural!")

    else:
        raise TypeError("The input must be an integer!")


def get_not_prime_list(number):
    '''Get the list of the numbers that are not prime up to the input number'''

    # Check for a positive integer input
    if type(number) == int:
        if number > 0:
            my_list = []

            # Test if numbers are not prime and add them to the not prime list
            for i in range(2, number + 1):
                if not is_prime(i):
                    my_list.append(i)
            
            return my_list
        
        else:
            raise ValueError("The number must be a natural!")
    
    else:
        raise TypeError("The input must be an integer!")


def get_prime_decomposition(number):
    '''Get the number factorized into prime numbers'''

    exponents = []
    primes = get_prime_list(number)

    # Test if primes are divisors
    for i in range(len(primes)):
        prime_exponent = 0

        # Check how many times the number can be divided by the prime
        while number % primes[i] == 0:
            number /= primes[i]
            prime_exponent += 1

        exponents.append(prime_exponent)

    return primes, exponents


def solution(number):
    '''Solution 5: Get the smallest positive number that is evenly divisible
    by all of the numbers from 1 up to the input number'''

    primes = get_prime_list(number)
    not_primes = get_not_prime_list(number)
    exponents = [1 for i in range(len(primes))]
    
    # Decompose not prime numbers into prime numbers
    for number in not_primes:
        n_pri, n_ex = get_prime_decomposition(number)

        # Check if the prime decomposition exponent were taken into account
        for i in range(len(n_pri)):
            if n_ex[i] > exponents[i]:
                exponents[i] = n_ex[i]

    # Get the desired number
    result = 1
    for i in range(len(primes)):
        result *= primes[i]**exponents[i]

    return result
