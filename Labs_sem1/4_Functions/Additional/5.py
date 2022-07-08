def type_by_sides(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    "acute triangle"
    >>> type_by_sides(3, 4, 5)
    "right angled triangle"
    >>> type_by_sides(3, 4, 6)
    "obutuse triangle"
    >>> type_by_sides(3, 3, 2015)

    """
    sides=[a,b,c]
    '''
    for i in  range(len(sides)): 
        if sides[i] >= sides[(i+1)%3]+sides[(i-1)%3] :
            return None

    for i in  range(len(sides)):
        if sides[i]**2 == sides[(i+1)%3]**2+sides[(i-1)%3]**2:
            return 'right angled triangle'
        if sides[i]**2 > sides[(i+1)%3]**2+sides[(i-1)%3]**2:
            return 'obutuse triangle'
    
    return 'acute triangle'
    '''

    longest_side=max(sides)
    print(longest_side)
    sides.remove(longest_side)

    if longest_side >= sides[0] + sides[1]:
        return None
    elif longest_side**2 > sides[0]**2 + sides[1]**2 :
        return 'obutuse triangle'
    elif longest_side**2 > sides[0]**2 + sides[1]**2 :
        return 'right angled triangle'  
    else :
        return 'acute triangle'
    

print(type_by_sides(3,4,5))
#done