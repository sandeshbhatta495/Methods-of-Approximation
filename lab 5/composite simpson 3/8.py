def f(x):
    return 1 + x**3  # Example function

a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals n (must be multiple of 3): "))


h = (b - a) / n
result = f(a) + f(b)

for i in range(1, n):
    x_i = a + i * h
    if i % 3 == 0:
        result += 2 * f(x_i)
    else:
        result += 3 * f(x_i)

integral = (3 * h / 8) * result
print(f"The estimated value of the integral using Composite Simpson's 3/8 Rule is: {integral:.4f}")
