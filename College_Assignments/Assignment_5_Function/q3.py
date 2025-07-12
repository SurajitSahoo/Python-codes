def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18
print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")  # Output: GCD of 48 and 18 is 6
