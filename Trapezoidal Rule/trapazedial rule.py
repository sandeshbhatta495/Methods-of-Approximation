#trapazedial rule
def func(x):
    return 1 + x**3

def trapezoidal(func,a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(1,n):
        x=a+i*h
        sum+=func(x)
    return (h/2)*(func(a)+func(b)+2*sum)

n=int(input("Enter the number of subintervals: "))
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
print(trapezoidal(func,a,b,n))
 


