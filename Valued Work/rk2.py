x0=float(input("x0: "))
y0=float(input("y0: "))
xn=float(input("xn: "))
h=float(input("h: "))

def func(x0,y0,xn,h):
    n=round((xn-x0)/h)
    for i in range(n):
        m1=func(x0,y0)
        m2=func(x0+h/2,y0+h/2*m1)
        yn= y0+h/2(m1+m2)
        x0+=h
        y0=yn
    print(f"The value of y at x = {xn} is {y0:.4f}")

func(x0,y0,xn,h)