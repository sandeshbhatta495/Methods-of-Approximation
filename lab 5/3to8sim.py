def f(x):
    return 1 + x**3  # Example function

a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))

h = (b - a) / 3

x1 = a + h
x2 = a + 2 * h

integral = (3 * h / 8) * (f(a) + 3*f(x1) + 3*f(x2) + f(b))

print(f"The estimated value of the integral using Simpson's 3/8 Rule is: {integral:.4f}")
