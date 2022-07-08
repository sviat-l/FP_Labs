def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(120, 30, 30)
    'obutuse triangle'
    >>> type_by_angles(100.5, 40, 39.5)
    'obutuse triangle'
    >>> type_by_angles(70, 50.5, 59.5)
    'acute triangle'
    >>> type_by_angles(45.6,44.4,90)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    """
    if a+b+c !=180:
        return None

    biggest_angle=max(a,b,c)

    if biggest_angle>90:
        return "obutuse triangle"
    elif biggest_angle==90:
        return "right angled triangle"
    else:    
        return "acute triangle"

print(type_by_angles(30.1,119.9,30.0))

#done
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())