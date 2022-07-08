import math


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    (float, float, float, float, float, float, float, float, float, float) -> float
    Find and return the area of the quadrangle by its sides line coeficients
    rounded to 2 digits after point.
    """
    vertices=[]
    vertices.append(lines_intersection(k1, c1, k2, c2))
    vertices.append(lines_intersection(k2, c2, k3, c3))
    vertices.append(lines_intersection(k3, c3, k4, c4))
    vertices.append(lines_intersection(k4, c4, k1, c1))
    #check if polygon is self-intersected
    intersection, intersection_point = self_intersection_check(vertices)
    if intersection:
        #calculate area of the self intersected
        area = (abs(cross_product(vertices[0], intersection_point, vertices[1])) +\
                abs(cross_product(vertices[2], intersection_point, vertices[3])))/2
    else:
        #calculate are of the polygon even if it is comvex
        area = abs(cross_product(vertices[1], vertices[0], vertices[2]) +\
                cross_product(vertices[2], vertices[0], vertices[3]))/2

    return area


def lines_intersection(k1, c1, k2, c2):
    """
    (float, float,float, float)-> tuple
    Find and return tuple with coordinates of point of the intersection
    of two lines rounded to 3 digits after point.
    If they don't intersect function should return None
    """
    if k1==k2:
        return None
    x=(c2-c1)/(k1-k2)
    y=k1*x+c1
    return (round(x, 3), round(y, 3))


def distance(coord1, coord2):
    """
    (tuple, tuple) -> float
    Find and return the distance beetwen 2 points by their coordinates
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


def cyclic_quadrilateral_check(vertix1, vertix2, vertix3, vertix4):
    """
    (tuple, tuple,tuple, tuple) -> bool
    Function checks wheather the quidrilateral is cyclic.
    Return True  if it is. Else return False
    """
    if distance(vertix1,vertix3)*distance(vertix2,vertix4) ==\
    distance(vertix1,vertix3)*distance(vertix2,vertix4) +\
    distance(vertix1,vertix3)*distance(vertix2,vertix4):
        return True
    return False

def cyclic_quadrilateral_area(vertix1, vertix2, vertix3, vertix4):
    """
    (tuple, tuple,tuple, tuple) -> float
    Function finds and return the quidrilateral area
    By its vertix coordinates.
    """


    side_1 = distance(vertix1,vertix2)
    side_2 = distance(vertix2,vertix3)
    side_3 = distance(vertix3,vertix4)
    side_4 = distance(vertix4,vertix1)

    if side_1 + side_2 == side_3 + side_4:
        return side_1**2

    semi_p = (side_1+side_2+side_3+side_4)/4

    return math.sqrt((semi_p-side_1)*(semi_p-side_2)*(semi_p-side_3)*(semi_p-side_4))


def cross_product(point_previous, point, point_next):
    """
    (tuple, tuple, tuple) -> float
    Calculate and return vector product by 3 points points coordinates.
    (vectors by points are 1->2 and 2->3)
    """
    vector1_x = point[0] - point_previous[0]
    vector2_x = point_next[0] - point[0]
    vector1_y = point[1] - point_previous[1]
    vector2_y = point_next[1] - point_previous[1]

    return vector1_x * vector2_y - vector2_x * vector1_y


def comvex_check(vertices):
    """
    list - > bool:
    Check by  wheather polygon is convex  by list of its vertices coordinates.
    Return True if yes, False if not.
    """
    if  cross_product(vertices[-2], vertices[-1], vertices[0]) < 0:
        cross_product_sigh = -1
    else:
        cross_product_sigh = 1

    number_of_vertices = len(vertices) -1
    for current_vertix in range(number_of_vertices):

        vertix_cross_product = cross_product(vertices[current_vertix - 1],
                                             vertices[current_vertix],
                                             vertices[current_vertix + 1 ])

        if vertix_cross_product * cross_product_sigh < 0:
            return False

    return True


def side_line_equation(point1, point2):
    """
    (tuple, tuple) -> tuple
    Calculate and return coeficients of a line on which is
    a side of the polygon  by side vertixes coordinates.
    """
    k = (point1[1] - point2[1])/(point1[0] - point2[0])
    b = point1[1] - k * point1[0]

    return k,b


def self_intersection_check(vertices):
    """
    Check if the polynom has self-intersections.
    Polynom is given by its vertices coordinates.
    Return True if it is self-intersected, also return coordinates of that point
    Return False if not.
    """

    line_coefficients=[]
    vertix_number = len(vertices) -1

    x, y = 0, 1
    # add lines coeffs of the polygon sides to the list
    for i in range( vertix_number, -1, -1):
        temp_k, temp_b = side_line_equation(vertices[i],vertices[i-1])
        line_coefficients.append(temp_k, temp_b)

    line_coefficients = line_coefficients[::-1]


    for current_vertix in range(vertix_number, 0, -1):

        for j in range (current_vertix - 2, -1, -1):
            #find x-coord of two lines intersection (current side and j-side)
            x_intersection = lines_tuple_intersection(line_coefficients[current_vertix],
                                                    line_coefficients[j]) [x]
            # check if lines intersect on a side
            if x_intersection  in range( min(vertices[i][x], vertices[i-1][x]),
                                        max(vertices[i][x], vertices[i-1][x])):
                if not (current_vertix == vertix_number and j == 0):
                    y_intersection =  x_intersection * line_coefficients[j][x] +\
                                                       line_coefficients[j][y]
                    return True, (x_intersection, y_intersection)

    return False, (None, None)


def lines_tuple_intersection(line1_coefs, line2_coefs):
    """
    (tuple, tuple)-> tuple
    Find and return tuple with coordinates of point of the intersection
    of two lines rounded to 3 digits after point.
    If they don't intersect function should return None
    """
    if line1_coefs[0]==line2_coefs[0]:
        return None
    x = (line2_coefs[1] - line1_coefs[1]) / (line1_coefs[0]- line2_coefs[0])
    y = line1_coefs[0] * x + line2_coefs[1]

    return (round(x, 3), round(y, 3))


def point_to_line_distance(point, line):
    """
    (tuple, tuple) -> float
    Calculate  and return distance between  point (given by its coordinates)
    and the line (given by its coefficients)
    """
    return (abs(line[0] * point[0] - point[1] + line[1])/
                                         math.sqrt(line[0]**2 +1))
