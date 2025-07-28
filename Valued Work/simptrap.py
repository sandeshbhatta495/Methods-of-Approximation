#composite trapezodial rule 
# function 
def func(x):
    return 1+x**3

a=int(input("Enter a:"))
b=int (input("enter b:"))
n=int (input("no of strib :"))

h=(b-a)/n

sum =0

#formula for simple trapezoidal rule 
for i in range (1,n-1):
    i=h/2* (func(a) + func(b)+ 2*func(a+i*h))



print ("value ",i)