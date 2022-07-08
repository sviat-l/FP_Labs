def polynomials_multiply(polynom1, polynom2):
    """
    (list,list) -> list
    Find and return coeficients of the polynom gotten by the multiplication 
    of two  polynoms

    >>> polynomials_multiply([2], [3])
    [6]
    >>> polynomials_multiply([2,-4],[3,5])
    [6, -2, -20]
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6, 0, -8, 0, -8, 0]

    """
    len_1=len(polynom1)
    len_2=len(polynom2)
    result=[0]*(len_1+ len_2-1)

    for i in range (len_1):
        for j in range (len_2):
            result[i+j] +=polynom1[i]*polynom2[j]

    return result

print(polynomials_multiply([2,0,-4],[3,0,2,0]))
#done


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())