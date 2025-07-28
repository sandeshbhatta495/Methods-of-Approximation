import math

def equation(x):
    return 2 / ((x + 1) ** 2)

x0 = float(input("Enter first guess: "))
e = float(input("Enter tolerable error: "))
max_iter = 100

i = 1
x1 = equation(x0)

while abs(x1 - x0) > e and i <= max_iter:
    print(f"Iteration {i}: x = {x1:.6f}")
    x0 = x1
    x1 = equation(x0)
    i += 1

if i > max_iter:
    print("Method did not converge.")
else:
    print(f"\nRoot is approximately: {x1:.6f}")
    print(f"Converged in {i - 1} iterations.")
