try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("The number cannot be negative.")
    print(f"The number is: {num}")
except ValueError as e:
    print(f"Error: {e}")
