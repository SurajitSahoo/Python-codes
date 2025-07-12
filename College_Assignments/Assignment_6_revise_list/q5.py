numbers = range(1, 21)  # List of numbers from 1 to 20
result = list(filter(lambda x: x % 2 == 0 or x % 3 == 0, numbers))
print(result)
