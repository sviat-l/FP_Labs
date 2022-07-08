def polygon_area(vertices):
    """
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    area=0
    number_of_verticec=len(vertices)
    for current_vertix in range(number_of_verticec):
        area+= vertices[current_vertix][0] * vertices[(current_vertix+1)% number_of_verticec][1] 
        area-= vertices[current_vertix][1] * vertices[(current_vertix+1)% number_of_verticec][0] 
    return abs(area/2)

print(polygon_area([(9,7), (11,2), (2,2), (4, 10)]))
#done