def f(x):
  
    return 1+x**3

def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Step size
    result = f(a) + f(b)  # First and last terms
    
    for i in range(1, n):
        x = a + i * h
        result += 2 * f(x)
    
    result *= (h / 2)
    return result

a=int(input("enter the first limit "))
a=int(input("enter the second  limit "))
h=int(input("enter the step size  "))


approx_integral = trapezoidal_rule(a, b, n)
print(f"Approximate integral using Trapezoidal Rule: {approx_integral}")
