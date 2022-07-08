"""Calculus module"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def find_max_1(function, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    >>> find_max_1('5 * x ** 2 - x ** 4 - 14', [1, 2, 3, -1])
    -10
    >>> find_max_1(lambda x: - x ** 3 - 99 * x, [1, 10, 37, 45, 57])
    -100
    >>> find_max_1(' - x ** 2 + x', [1, 0, 2, -2])
    0
    >>> find_max_1(lambda x: - x ** 101 + x**57 + x** 3, [1])
    1
    """
    if isinstance(function, str):
        return max(eval(function, {'x': point}) for point in points )
    return max(function(point) for point in points)

# print(find_max_1('x ** 2 + x', [1, 2, 3, -1]))

def find_max_2(function, points):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> find_max_2('5 * x ** 2 - x ** 4 - 14', [1, 2, 3, -1])
    [1, 2, -1]
    >>> find_max_2(lambda x: - x ** 3 - 99 * x - 27 *  x ** 5, [1, 10, 37, 45, 57])
    [1]
    >>> find_max_2(' - x ** 2 + x', [1, 0, 2, -2])
    [1, 0]
    >>> find_max_2(lambda x: - x ** 101 + x**57 + x** 3, [1])
    [1]
    """
    dict_f = {}
    if isinstance(function, str):
        for point in points:
            dict_f[eval(function, {'x': point})] = dict_f.get(eval(function, {'x': point}), [])\
                                                   + [point]
    else:
        for point in points:
            dict_f[function(point)] = dict_f.get(function(point), []) + [point]
    return dict_f[max(dict_f)]


def compute_limit(sequence):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    >>> compute_limit('(172 * n ** 5 + n ** 2 - 3463 * n) / n ** 5 / 10')
    17.2
    >>> compute_limit(lambda n: (-7 * n ** 4 - 77 * n ** 3 + 12*n) / n ** 4 / 10)
    -0.7
    >>> compute_limit(lambda n: (325 * n ** 14 + 665 * n ** 7 + 228 * n) / n ** 15)
    0.0
    """
    iterration = 0
    if isinstance(sequence, str):
        limit_iteration1 = eval(sequence, {'n': 1})
        while True:
            limit_iteration2 = eval(sequence, {'n': 10 ** (iterration + 1)})
            if abs(limit_iteration2 - limit_iteration1) < 0.001:
                return round(limit_iteration2, 2)
            limit_iteration1 = limit_iteration2
            iterration +=1
    limit_iteration1 = sequence(1)
    while True:
        limit_iteration2 = sequence(10 ** (iterration + 1))
        if abs(limit_iteration2 - limit_iteration1) < 0.001:
            return round(limit_iteration2, 2)
        limit_iteration1 = limit_iteration2
        iterration +=1


def compute_derivative(func, x_var):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    >>> compute_derivative('x ** 2 - 5 * x', 100)
    195.0
    >>> compute_derivative(lambda x: 12* x ** 2 + 36 * x - 11, -10)
    -204.0
    >>> compute_derivative('x ** 54 + x ** 17 - x **2 + 5436', 0)
    -0.0
    >>> compute_derivative(lambda x: 7 * x ** 2 + 13 * x, -1)
    -1.0
    """
    iterration = -1
    if isinstance(func, str):
        function_value = eval(func, {'x':x_var})
        derivative_1 = eval(func, {'x':x_var+1}) - function_value
        while True:
            derivative_2 = (eval(func, {'x':x_var + 10 ** iterration}) - function_value)\
                            / 10 ** iterration
            if abs(derivative_2 - derivative_1) < 0.001:
                return round(derivative_2, 2)
            derivative_1 = derivative_2
            iterration -= 1
    function_value = func(x_var)
    derivative_1 = func(x_var + 1) - function_value
    while True:
        derivative_2 = (func(x_var + 10 ** iterration) - function_value) / 10**iterration
        if abs(derivative_2 - derivative_1) < 0.001:
            return round(derivative_2, 2)
        derivative_1 = derivative_2
        iterration -= 1


def get_tangent(function, varb_x):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, -2)
    '5.0 * x + 4.0'
    >>> get_tangent('- x ** 2 + x', 0)
    '1.0 * x + 0.0'
    >>> get_tangent(lambda x: x ** 2 + x, 100)
    '201.0 * x - 10000.0'
    >>> get_tangent('- x ** 3 + 3* x **2 + 9 * x', -1)
    '0.0 * x - 5.0'
    """
    k_coef = compute_derivative(function, varb_x)
    b_coef = eval(function, {'x':varb_x}) - varb_x * k_coef if isinstance(function, str)\
             else function(varb_x) - varb_x * k_coef
    result = f'- {-k_coef} * x ' if k_coef < 0 else f'{k_coef} * x '
    result += f'- {-b_coef}' if b_coef < 0 else f'+ {b_coef}'
    return result

def get_root(function, a_var, b_var):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root('2 * x + 3', -2, 55)
    -1.5
    >>> get_root(lambda x: x ** 3 - 10 * x ** 2 -  x, 10, 20)
    10.1
    >>> get_root(' 4 * x ** 3 + 16 * x ** 2 + 16', -11, -1)
    -4.22
    >>> get_root(lambda x: x ** 2 - 18 * x - 40  , 0, 77)
    20.0
    """
    def value_sigh(value, function = function):
        if isinstance(function, str):
            if eval(function,{'x': value}) == 0:
                return 0
            return  1 if eval(function,{'x': value}) > 0 else -1
        if function(value) == 0:
            return 0
        return 1 if function(value) > 0 else  -1

    left_var, right_var = a_var, b_var
    right_sigh =value_sigh(right_var)
    while True:
        if abs(left_var - right_var) < 0.001:
            return round(left_var, 2)
        average_var = (left_var + right_var) / 2
        avarage_sigh = value_sigh(average_var)
        if avarage_sigh == 0:
            return round(average_var,2)
        if avarage_sigh == right_sigh:
            right_var = average_var
        else:
            left_var = average_var

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())