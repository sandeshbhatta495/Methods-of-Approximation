def func(x,y):
    return 1 + 3 * x ** 2

def euler(x0, y0, xn, h):
    n = round((xn - x0) / h)
    print("\nx0\t y0\t m\t\t yn")
    for i in range(n):
        m = func(x0, y0)
        yn = y0 + h * m
        print(f"{x0:.2f}\t{y0:.2f}\t{m:.2f}\t{yn:.2f}")
        x0 += h
        y0 = yn
    print(f"\nThe value of y at x = {xn} is {y0:.2f}")

x0, y0,xn,h = float(input("x0: ")), float(input("y0: ")), float(input("xn: ")) , float(input("Step size h: "))
euler(x0, y0, xn, h)
