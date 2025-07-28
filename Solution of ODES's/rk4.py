def func(x, y):
    return 1 + 3 * x ** 2

def euler(x0, y0, xn, h):
    n = round((xn - x0) / h)
    print("\nx0\t\ty0\t\tm\t\tyn")
    for i in range(n):
        m1 = func(x0, y0)
        m2=func(x0+h/2,y0+h/2*m1)
        m3=func(x0+h/2,y0+h/2*m2)
        m4=func(x0+h,y0+h*m)
        yn = y0 + h*(m+2*m2+2*m3+m4)/6 
        print(f"{x0:.2f}\t\t{y0:.4f}\t\t{m1:.4f}\t\t{yn:.4f}")
        x0 += h
        y0 = yn
    print(f"\nThe value of y at x = {xn} is {y0:.4f}")

try:
    x0 = float(input("x0: "))
    y0 = float(input("y0: "))
    xn = float(input("xn: "))
    h = float(input("Step size h: "))
    euler(x0, y0, xn, h)
except ValueError:
    print("Please enter valid numeric values.")
