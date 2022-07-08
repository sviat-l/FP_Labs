import math
def temp(k):
    return math.factorial(6*k)/(math.factorial(3*k)*math.factorial(k)**3)

for i in range (10000000000000000,10000000000000005):
    f1=8*(6*i+1)*(6*i+3)*(6*i+5) 
    f2=(i+1)**3
    print(round(f1/f2, 15))

