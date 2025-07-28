# Composite Simpson's 3/8 Rule

def func(x):
    return 1 + x**3

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of strips (must be multiple of 3): "))

# Check if n is a multiple of 3
if n % 3 != 0:
    print("Error: n must be a multiple of 3 for Simpson's 3/8 Rule.")
    exit()

# Step size
h = (b - a) / n

# Initialize sums
sum_3 = 0  # For i = multiples of 3 (except 0 and n)
sum_rest = 0  # For all others

for i in range(1, n):
    x = a + i * h
    if i % 3 == 0:
        sum_3 += func(x)
    else:
        sum_rest += func(x)

# Apply Simpson's 3/8 formula
result = (3 * h / 8) * (func(a) + 3 * sum_rest + 2 * sum_3 + func(b))

print("Value using Composite Simpson's 3/8 Rule:", result)
