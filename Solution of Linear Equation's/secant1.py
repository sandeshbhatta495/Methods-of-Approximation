import math
def f(x):
    return x**2 - 4*x - 10

x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

step = 1
print('\n\n*** Secant METHOD IMPLEMENTATION ***')
print('\n step\t\tx0\t\tf(x0)\t\tx1\t\tf(x1)\t\tx2\t\tf(x2)')
x2=x0
f2=f(x2)

while abs(f2)>e:
    x2=(x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    f2=f(x2)
    print(step,"\t\t",x0,"\t\t",f(x0),"\t\t",x1,"\t\t",f(x1),"\t\t",x2,"\t\t",f(x2))
    x0=x1
    x1=x2
    step+=1
print("\n Required Root is: %0.8f" % x2)
print("\n\n")
print("Itteration:",step-1)

