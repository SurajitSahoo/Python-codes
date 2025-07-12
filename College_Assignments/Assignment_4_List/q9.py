list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

common_member = any(x in list2 for x in list1)
print(common_member)  # Output: True
