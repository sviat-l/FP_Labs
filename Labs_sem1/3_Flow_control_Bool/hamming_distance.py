x, y = input("Enter two values: ").split()
x=int(x)
y=int(y)
weight=0
while x>0:
    if (x&1) ^ (y&1) :
        weight+=1
    x>>=1
    y>>=1
print(weight)