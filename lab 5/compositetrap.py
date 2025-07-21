# Step 1: Start

# Step 2: Define the function to integrate
def f(x):
    return 1+x**3  # Example function: f(x) = x^2

a=1
b=2
# Step 3: Input the limits and number of subintervals
# a = float(input("Enter the lower limit a: "))
# b = float(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals n: "))

# Step 4: Calculate the step size
h = (b - a) / n

# Step 5: Initialize the result with f(a) and f(b)
result = f(a) + f(b)

# Step 6: Loop through intermediate points and add 2*f(x_i)
for i in range(1, n):
    x_i = a + i * h
    result += 2 * f(x_i)

# Step 7: Multiply by h/2 to get final integral
integral = (h / 2) * result

# Step 8: Display the result
print(f"The estimated value of the integral using Composite Trapezoidal Rule is: {integral:.2f}")
