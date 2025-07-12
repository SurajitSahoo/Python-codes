# Original list with both positive and negative values
numbers = [10, -5, 20, -15, 30, -25, 40]

# Using filter() to create a list with only positive values
positive_numbers = list(filter(lambda x: x > 0, numbers))

# Output the list of positive numbers
print(positive_numbers)
