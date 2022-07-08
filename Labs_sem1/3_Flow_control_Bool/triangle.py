starting_number=int(input())
num_of_lines=int(input())
for left_lines in range (num_of_lines,0,-1):
    for current_position in range(left_lines-1):
        print(starting_number+current_position, end=' ')
    print(starting_number+left_lines-1)