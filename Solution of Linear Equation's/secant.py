import math
def function(x):
    return 4*math.sin(x)- math.exp(x)

x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

step = 1
print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
print('\n step\t\tx0\t\tfunction(x0)\t\tx1\t\tfunction(x1)\t\tx2\t\tfunction(x2)')
x2=x0
f2=function(x2)

while abs(f2)>e:
    x2=(x0*function(x1)-x1*function(x0))/(function(x1)-function(x0))
    f2=function(x2)
    print(step,"\t\t",x0,"\t\t",function(x0),"\t\t",x1,"\t\t",function(x1),"\t\t",x2,"\t\t",function(x2))
    x0=x1
    x1=x2
    step+=1
print("\n Required Root is: %0.8f" % x2)
print("Itteration:",step-1)

