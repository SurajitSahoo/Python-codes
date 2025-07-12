def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
number = int(input("Enter number : "))
print(f"Factorial of {number} is {factorial(number)}")  # Output: Factorial of 5 is 120
