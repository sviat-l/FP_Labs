import math


def sales_prediction():
    print(1.19*float(input()))
    
def yard_to_meter():
    l=float(input())
    print(round((0.914*l*10**3), 4))
    print(round((0.914*l), 4))
    print(round((0.914*l*10**-3), 6))

def cashier():
    sum1=float(input())
    sum2=float(input())
    sum3=float(input())
    sum4=float(input())
    sum5=float(input())
    total=sum1+sum2+sum3+sum4+sum5    
    print(round((total), 4))
    print(round((total*0.14), 4))
    print(round((total*1.14), 4))

def odometer():
    v=float(input())
    a=float(input())
    t1=float(input())
    t2=float(input())
    if v+a*t1<0:
        t=abs(v/a)
        s1=v*t+0.5*a*t**2 + abs(0.5*a*(t1-t)**2)
    else: s1=v*t1+0.5*a*t1**2
    s2=abs((v+a*t1)*t2)
    print(round((s1+s2), 4))

def payment_instalments():
    price=float(input())
    num_of_install=float(input())
    print(round((1.05*price), 4))
    print(round((1.05*price/num_of_install), 4))


def miles_per_galon():
    driven=float(input())
    gas_used=float(input())
    print(round((driven/gas_used), 4))



def cookie():
    cooki_e=float(input())
    print(round((1.5*cooki_e/48), 4))
    print(round(((1*cooki_e)/48), 4))
    print(round(((2.75*cooki_e)/48), 4))


def vineyard():
    row=float(input())
    lenght=float(input())
    distance=float(input())
    number=int(((row-2*lenght)/distance)//1)
    print(number)


def compound_interest():
    p=float(input())
    r=float(input())
    n=float(input())
    t=float(input())
    a=p*(1+r/100/n)**(n*t)
    print(round(a, 4))


if __name__ == "__main__":
    eval(input() + "()")
