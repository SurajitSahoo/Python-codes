# Sample lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Using map() to add corresponding elements of both lists
result = list(map(lambda x, y: x + y, list1, list2))

# Output the result
print(result)
