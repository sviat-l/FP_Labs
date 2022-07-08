import math


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    (float, float,float, float,float, float,float, float,float, float) -> float
    Find and return the area of the quadrangle by its sides line coeficients
    rounded to 2 digits after point.
    """
    vertices=[]
    vertices.append(lines_intersection(k1, c1, k2, c2))
    vertices.append(lines_intersection(k2, c2, k3, c3))
    vertices.append(lines_intersection(k3, c3, k4, c4))
    vertices.append(lines_intersection(k4, c4, k1, c1))

    if k1==k3:
        height=parallel_lines_distance( k1, c1, c3)
        medium_line = (distance(vertices[0], vertices[3]) + distance(vertices[1], vertices[2]))/2
    elif k2==k4:
        height=parallel_lines_distance( k2, c2, c4)
        medium_line = (distance(vertices[0], vertices[1]) + distance(vertices[3], vertices[2]))/2
    else:
        return "quadrilateral doesn't have sides on parallel lines"

    return round((height * medium_line), 2)


def lines_intersection(k1, c1, k2, c2):
    """
    (float, float,float, float)-> tuple
    Find and return tuple with coordinates of point of the intersection
    of two lines rounded to 3 digits after point.
    If they don't intersect function should return None
    """
    if k1==k2:
        return None
    return (round((c2-c1)/(k1-k2), 3), round(k1*(c2-c1)/(k1-k2) + c1, 3))


def distance(coord1, coord2):
    """
    (tuple, tuple) -> float
    Find and return the distance beetwen 2 points with their coordinates
    rounded to 3 digits after point.
    """
    return round(math.sqrt( (coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2), 3)


def parallel_lines_distance(k, b1, b2):
    """
    (float, float,float) -> float
    Find and return the distance between parallel lines by lines' coefficients
    rounded to 3 digits after point.
    """
    return round(abs(b1-b2)/k/math.sqrt(k**2+1), 3)

print(four_lines_area(1, 1, -1, 1, 1, -1, -1, -1))
