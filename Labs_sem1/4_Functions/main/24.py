def numbers_Ulam(n):
    """
    int -> list
    Return sequence of first n Ulam numbers.
    
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    >>> numbers_Ulam(25)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97]
     """

    
    if n==1:    return [1]
    ulan=[1,2]

    for position in range (2,n):
        temp_list=[0]*(ulan[position-1]+ulan[position-2])

        for i in range(len(ulan)-1):
            for j in range(i+1, len(ulan)):
                if (ulan[i]+ulan[j] )not in ulan:
                    temp_list[ulan[i]+ulan[j]-1]+=1

        ulan.append(temp_list.index(1)+1)

    return ulan
            
print(numbers_Ulam(25))         
#done

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())