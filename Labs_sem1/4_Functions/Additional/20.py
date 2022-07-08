def polynomial_eval(coefficients, value):
    """
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    result=0
    polynom_exponent=len(coefficients)-1
    for current_exponent in range(polynom_exponent+1):
        result+= coefficients[current_exponent] * value** (polynom_exponent -  current_exponent)
    return result

print(polynomial_eval( [2,3,0,4], 4))
#done