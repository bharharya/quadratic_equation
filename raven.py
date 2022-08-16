import math
def quadratic(a,b,c):
    if a==0:
        print('give another number')
    else:
        d=math.sqrt((b**2)-(4*a*c))
        e=((-(b)+d)/(2*a))
        f=((-b-d)/(2*a))
        print(str(e))
        print(str(f))
