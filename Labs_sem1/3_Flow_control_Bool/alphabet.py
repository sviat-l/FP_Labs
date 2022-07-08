import math
n=int(input())
row_number= math.ceil( 0.5*((1+8*n)**0.5 -1) )
ord_character=65

for current_row in range(row_number):
    print(' '*2*(row_number-current_row-1), end='')
    for i in range(current_row+1):
        if i==current_row  or ord_character==64+n: 
            print(chr(ord_character))
        else:
            print(chr(ord_character), end=' ')
        ord_character+=1