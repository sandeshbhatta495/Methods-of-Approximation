import math
def function(x):
    return x*math.tan(x)-1
def derivative(x):
    return (x/math.cos(x)**2+ math.tan(x))

x0 = float(input('First Guess: '))
e = float(input('Tolerable Error: '))

step = 1
print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
print('\n step\t\tx0\t\tfunction(x0)\t\tx1\t\tfunction(x1)\t\tx2\t\tfunction(x2)')
x1=x0
f1=function(x1)

while abs(f1)>e:
    x1=x0-f1/derivative(x0)
    f1=function(x1)
    print(step,"\t\t",x0,"\t\t",function(x0),"\t\t",x1,"\t\t",function(x1))
    x0=x1
    step+=1
print("Root is ","%.4f" % x1)
print("\n\n")
print("Itteration:",step-1)

