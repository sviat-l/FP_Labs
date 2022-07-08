def generate_number(number, digit, position):
    """
    Take a number and returns a new one with a digit
    inserted in a given position if digit is bigger
    then initital digit in position

     >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    >>> generate_number(3746, 5, 3)
    5746
    >>> generate_number(3746, 5, 4)
    53746
    >>> generate_number(3746, 5, 7)
    50003746
    >>> generate_number(-12345, 9, 10)
    -90000012345
    """
    sign=1
    if number<0:
        sign=-1

    digit_by_number=(abs(number)//10**(position))%10
    if  digit_by_number< digit:
        number+= sign*(digit - digit_by_number) * 10**position

    return number
    
print(generate_number(-3746, 5, 4))
#done