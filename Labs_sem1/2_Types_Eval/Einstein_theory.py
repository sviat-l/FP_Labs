import math
m=float(input())
v=float(input())
E=m*(299792458.0**2)/math.sqrt(1-(v/299792458.0)**2)
print(E)