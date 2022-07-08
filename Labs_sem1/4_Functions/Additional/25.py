def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    sequance=[n]
    while True:
        a_next=0
        a_previous=sequance[-1]

        while  a_previous>0:
            a_next+=(a_previous%10)**2
            a_previous//=10
        
        if  a_next==4  or a_next in sequance :
            return False
            
        if a_next==1:
            return True
        
        sequance.append(a_next)

print(happy_number(20))

#done