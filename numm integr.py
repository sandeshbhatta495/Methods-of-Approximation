def func(x):
    return x*x

a=float(input("A:"))
b=float(input("b:"))
n=int(input("h:"))

h=(b-a)/n

sum =0
for i in range(1,n):
    x=a+i*h
    sum += func(x)

result=(h/2)*(func(a)+ func(b)+2*sum)
print(result)
# def func(x):
#     return x**2  # Example function

# # Input from user
# a = float(input("Enter lower limit a: "))
# b = float(input("Enter upper limit b: "))
# n = int(input("Enter number of subintervals n: "))

# # Step size
# h = (b - a) / n

# # Apply Trapezoidal Rule
# total = 0
# for i in range(1, n):
#     x = a + i * h
#     total += func(x)

# # Final result
# result = (h / 2) * (func(a) + func(b) + 2 * total)

# print("Approximate integral:", result)
