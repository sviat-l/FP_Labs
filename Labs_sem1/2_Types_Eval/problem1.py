import math
r=float(input())
h=float(input())
V= round(float(h*math.pi*r**2), 3)
A=round(float(2*math.pi*r*(r+h)), 3)
print('V = ',V)
print('A = ',A)