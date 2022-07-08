output=''
num=int(input())

for add in range(1,num):
    output+=f'{2*add-1}/{2*add}'
    if add%2==1:
        output+=' - '
    else: 
        output+= ' + '
output+=f'{2*num-1}/{2*num}'

print(output)