

# Step 2: Define the function to integrate
def f(x):
    return 1 + x**3 

# Step 3: Input the lower and upper limits
a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
n=int(input("enter the number of subintervals n: "))

# Step 4: Calculate h
h = (b - a)/2  # Step size for Simpson's 1/3 Rule

# Step 5: Calculate the mid-point
mid = (a + b) / 2

# Step 6: Apply Simpson's 1/3 rule formula
integral =  h* (f(a) + 4 * f(mid) + f(b))/3

# Step 7: Display the result
print(f"The estimated value of the integral using Simpson's 1/3 Rule is: {integral:.4f}")

# Step 8: Stop
