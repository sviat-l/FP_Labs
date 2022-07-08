"""
Functions to work with happy numbers
"""

def happy_number(num):
    """
    int -> bool
    Check if num is happy. Return True if yes. False if not
    >>> happy_number(98766789)
    True
    >>> happy_number(7890000)
    False
    >>> happy_number(12909930)
    False
    >>> happy_number(123999)
    False
    >>> happy_number(4443333)
    True
    """
    first_sum, last_sum = 0, 0
    num_1 = num // 10000
    num_2 = num % 10000

    while num_1 > 9:
        first_sum += num_1 % 10
        num_1 //= 10

    while num_2 > 9:
        last_sum += num_2 % 10
        num_2 //= 10

    return first_sum + num_1 == last_sum + num_2



def happy_numbers(lowest, highest):
    """
    int -> int
    Expectation:
    -1 < n < 100000000 and m < n
    Return number of happy number that are in range (m, n+1)
    >>> happy_numbers(10000000,12345678)
    73116
    >>> happy_numbers(10000,56789)
    125
    >>> happy_numbers(1,10001)
    1
    >>> happy_numbers(1,10000)
    0
    """
    number_of_happy = 0
    for current_number in range(lowest, highest + 1):
        if happy_number(current_number):
            number_of_happy += 1
    return number_of_happy


def count_happy_numbers(number):
    """
    int -> int
    Expectation:
     -1 < n < 100000000
    Return number of 'happy numbers' that are <= n
    >>> count_happy_numbers(56784)
    125
    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10000)
    0
    >>> count_happy_numbers(10)
    0
    """
    number_of_happy = 0
    for current_number in range(1, number + 1):
        if happy_number(current_number):
            number_of_happy += 1
    return number_of_happy
