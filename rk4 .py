x0=float(input("x0: "))
y0=float(input("y0: "))
xn=float(input("xn: "))
h=float(input("h: "))

def func(x0,y0,xn,h):
    n=round((xn-x0)/h)
    for i in range(n):
        m1=func(x0,y0)
        m2=func(x0+h/2,y0+h/2*m1)
        m3=func(x0+h/2,y0+h/2*m2)
        m4=func(x0+h,y0+h*m1)
        yn= y0+h/6(m1+2*m2+2*m3+m4)
        x0+=h
        y0=yn
    print(f"The value of y at x = {xn} is {y0:.4f}")

func(x0,y0,xn,h)