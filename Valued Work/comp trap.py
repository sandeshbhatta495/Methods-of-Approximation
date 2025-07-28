# Composite Simpson's 1/3 Rule

# function definition
def func(x):
    return 1 + x**3

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of strips (even number): "))

if n % 2 != 0:
    print("Error: Number of strips must be even for Simpson's 1/3 Rule.")
    exit()
h = (b - a) / n

sum_odd = 0
sum_even = 0

for i in range(1, n):
    x = a + i * h
    if i % 2 == 0:
        sum_even += func(x)
    else:
        sum_odd += func(x)
result = (h / 3) * (func(a) + 4 * sum_odd + 2 * sum_even + func(b))
print("Value of integral using Composite Simpson's 1/3 Rule:", result)
