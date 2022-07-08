row_number=int(input())

for current_row in range (1,row_number+1):
    for symbol_position in range(1, current_row+1):
        if symbol_position==1 or symbol_position==current_row or row_number==current_row:
            print('*', end='')
        else:
            print(end=' ')
    print()