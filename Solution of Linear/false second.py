
import math 
# Defining Function
def f(x):
    return x**2 -4*x -10

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    print('\nf(x0) = %0.6f, f(x1) = %0.6f\n' % (f(x0), f(x1)))
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x0 = %0.6f, x1 = %0.6f, x2 = %0.6f and f(x2) = %0.6f' % (step, x0, x1, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.6f' % x2)

# Checking Correctness of initial guess values and bisecting
c=True
while c:
    # Input Section
    x0 = float(input('First Guess: '))
    x1 = float(input('Second Guess: '))
    e = float(input('Tolerable Error: '))
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        bisection(x0,x1,e)
        c=False

