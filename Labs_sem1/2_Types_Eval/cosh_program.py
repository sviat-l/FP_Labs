import math
x=float(input())
print("COS =", '{:.4f}'.format(math.cosh(x), 4))
print("EXP =", '{:.4f}'.format(0.5*(math.exp(x)+math.exp(-x)), 4))
print("E =", '{:.4f}'.format(0.5*(math.e**(x)+math.e**(-x)), 4))

