list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

difference = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
print(difference)  # Output: [1, 2, 3, 6, 7, 8]
