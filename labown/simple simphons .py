#simple trapezodial rule 
a=int(input("Enter a"))
b=int (input("enter b"))
h=(b-a)/2

# function 
def func(x):
    return 1+x**3
#formula for simple trapezoidal rule 
i=h/3* (func(a) + 4*func((a+b)/2)+func(b))

print ("value ",i)