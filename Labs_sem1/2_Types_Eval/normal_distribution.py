import math
x=float(input())
y=float(input())
z=float(input())
f=1/math.sqrt(2*math.pi*z**2)*math.exp(-0.5*((x-y)/z)**2)
print(round(f, 10))