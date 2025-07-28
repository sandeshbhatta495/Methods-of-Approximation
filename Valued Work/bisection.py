def f(x):
    return x**2 - 4*x - 10

def bisection(x0, x1, tol):
    while abs(f((x0 + x1)/2)) > tol:
        mid = (x0 + x1) / 2
        if f(x0) * f(mid) < 0:
            x1 = mid
        else:
            x0 = mid
    return (x0 + x1) / 2

while True:
    x0 = float(input("First guess: "))
    x1 = float(input("Second guess: "))
    tol = float(input("Tolerance: "))
    if f(x0) * f(x1) < 0:
        root = bisection(x0, x1, tol)
        print(f"Root ≈ {root:.6f}")
        break
    else:
        print("Invalid guesses. Try again.")
