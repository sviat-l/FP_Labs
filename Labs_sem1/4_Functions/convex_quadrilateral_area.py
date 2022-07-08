import math


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    (float, float,float, float,float, float,float, float,float, float) -> float
    Find and return the area of the quadrangle by its sides line coefficients
    rounded to 2 digits after point.
    """
    vertices = [[]]
    vertices.append(lines_intersection(k1, c1, k2, c2))
    vertices.append(lines_intersection(k2, c2, k3, c3))
    vertices.append(lines_intersection(k3, c3, k4, c4))
    vertices.append(lines_intersection(k4, c4, k1, c1))

    for i in vertices:
        if isinstance(i, type(None)):
            return None

    sides = []
    sides.append(distance(vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1]))
    sides.append(distance(vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1]))
    sides.append(distance(vertices[3][0], vertices[3][1], vertices[4][0], vertices[4][1]))
    sides.append(distance(vertices[4][0], vertices[4][1], vertices[1][0], vertices[1][1]))
    diagonal1 = distance(vertices[1][0], vertices[1][1], vertices[3][0], vertices[3][1])
    diagonal2 = distance(vertices[2][0], vertices[2][1], vertices[4][0], vertices[4][1])

    return quadrangle_area(sides[0], sides[1], sides[2], sides[3], diagonal1, diagonal2)


def lines_intersection(k1, c1, k2, c2):
    """
    (float, float,float, float)-> tuple
    Find and return tuple with coordinates of point of the intersection
    of two lines rounded to 2 digits after point.
    If they don't intersect function should return None
    """
    if k1 == k2:
        return None
    x = (c2-c1)/(k1-k2)
    y = k1*x+c1
    return round(x, 2), round(y, 2)


def distance(x1, y1, x2, y2):
    """
    (float, float,float, float) -> float
    Find and return the distance between 2 points with their coordinates
    rounded to 2 digits after point.
    """
    return round(math.sqrt((x1-x2)**2+(y1-y2)**2), 2)


def quadrangle_area(a, b, c, d, f1, f2):
    """
    (float, float,float, float,float, float) -> float
    Find and return the area of the quadrangle by sides' and diagonals' length
    rounded to 2 digits after point.
    """
    area_square = (4*f1**2*f2**2 - (b**2+d**2-a**2-c**2)**2) / 16
    if area_square < 0:
        return None
    return round(math.sqrt(area_square), 2)

print(quadrangle_area(3, 4, 3, 3, 1, 1))
print(four_lines_area(6,5,4,3,2,1,2,3))
print(quadrangle_area(3, 4, 3, 4, 5, 5))
