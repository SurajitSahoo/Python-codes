n = int(input("Enter the value of n: "))

sum_squares = sum(i**2 for i in range(2, n + 1, 2))

print(f"Sum of squares of even numbers up to {n}: {sum_squares}")
