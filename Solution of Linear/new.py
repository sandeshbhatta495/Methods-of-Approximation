import math
from math import exp
# Bisection Method to find the root of the equation 4*sin(x) - exp(x) = 0
def f(x):
    return 4*math.sin(x)-exp(x)
global x2

x0 = float(input("Enter first guess (x0): "))
x1 = float(input("Enter second guess (x1): "))
e = 0.001  

if f(x0) * f(x1) > 0:
    x0=x0
    print("choose another value ")

else:
    while abs(x1 - x0) >= e:
        x2 = (x0 + x1) / 2
        
        if f(x2) == 0:
            break
        elif f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        

print(f"Root is approximately: {x2}")