from functools import reduce

# Sample list
numbers = [1, 2, 3, 4, 5]

# Using reduce() to calculate the sum of the list elements
total_sum = reduce(lambda x, y: x + y, numbers)

# Output the sum
print(total_sum)
