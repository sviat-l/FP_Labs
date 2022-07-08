"""
program to generate pascal triangle
"""

def generate_pascal_triangle(rows):
    """
    Return pascal triangle by number of rows
    >>> print(generate_pascal_triangle(6))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    >>> print(generate_pascal_triangle(4))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> print(generate_pascal_triangle(1))
    [[1]]
    """
    if rows<=0 or not isinstance(rows, int):
        return []
    triangle = [[1]]
    for current_row in range(rows-1):
        triangle.append([1])
        for index_in_row in range(current_row):
            triangle[-1].append(triangle[-2][index_in_row] + triangle[-2][index_in_row + 1])
        triangle[-1].append(1)
    return triangle
