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
for i in range (1,n):
    x = a + h*i
    sum+=func(x)

i=h/2* (func(a) +2*sum + func(b) )


print ("Value of integral using Composite Trapezoidal Rule:",i)