"""
Fibonacci and factorial module
"""
import time
def factorial_iterative(number):
    """
    Return factorial of the number
    Expectation: number in natural number
    >>> factorial_iterative(2)
    2
    >>> factorial_iterative(10)
    3628800
    >>> factorial_iterative(50)
    30414093201713378043612608166064768844377641568960512000000000000
    """
    factorial = 1
    for cur_number in range(1,number + 1):
        factorial *= cur_number
    return factorial


def factorial_recursive(number):
    """
    Return factorial of the number
    Expectation: number in natural number
    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(11)
    39916800
    >>> factorial_recursive(49)
    608281864034267560872252163321295376887552831379210240000000000
    """
    return 1 if number < 2 else  number * factorial_recursive(number-1)


def fibonacci_recursive(number):
    """
    Return element of the fibonacci sequence with index number
    Expectation: number in natural number or 0
    >>> fibonacci_recursive(0)
    1
    >>> fibonacci_recursive(4)
    5
    >>> fibonacci_recursive(19)
    6765
    """
    return 1 if number < 2 else fibonacci_recursive(number-1) + fibonacci_recursive(number-2)

print(fibonacci_recursive(13))

def fibonacci_iterative(number):
    """
    Return element of the fibonacci sequence with index number
    Expectation: number in natural number or 0
    >>> fibonacci_iterative(1)
    1
    >>> fibonacci_iterative(6)
    13
    >>> fibonacci_iterative(28)
    514229
    """
    fibonacci_series = [1,1]
    for _ in range(number):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[number]

def numbers_time_test(function=0, realisation=0, verbose=False):
    """
    Return date with taken time for different functions and different number of iterations
    """
    if function and realisation:
        cur_function = fibonacci_iterative
    elif function and  not realisation:
        cur_function = fibonacci_recursive
    elif realisation:
        cur_function = factorial_iterative
    else:
        cur_function = factorial_recursive

    step = 5 if function else 100
    max_value = 39 if function else 900
    if verbose and not realisation:
        print('number          time              number of calls')
    else:
        print('number          time')
    for cur_number in range(1, max_value + 2, step):
        starting_time = time.time()
        result = cur_function(cur_number)
        taken_time =  time.time() - starting_time
        if verbose and not realisation:
            if function:
                taken_iterration = result
            else:
                taken_iterration = cur_number
            output_line = f'{cur_number:4}   {taken_time:<22}     {taken_iterration:<7} '
        else:
            output_line = f'{cur_number:4}   {taken_time:<22}'
        print(output_line)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    numbers_time_test(1,1, True)
    numbers_time_test(0,1)
    numbers_time_test(0,0, True)
    numbers_time_test(1,0, True)
