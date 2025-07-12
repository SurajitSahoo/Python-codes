# Accepting input values for x and y
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Lambda function to compute x^y
power = lambda x, y: x ** y

# Output the result
result = power(x, y)
print(f"The value of {x} raised to the power of {y} is: {result}")
