number=int(input())
position=0
while number>0:
    if number&1==1:
        print(position)
        exit()
    else:
        position+=1
        number>>=1

