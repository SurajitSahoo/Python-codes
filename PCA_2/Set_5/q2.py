#2. WAP to create a list with +ve and -ve values.Create another list using filter() that has only +ve values

mixed_values = [-10, -5, 0, 5, 10, 15, -20, 25, -30, 35]
positive_values = list(filter(lambda x: x > 0, mixed_values))

print("List with mixed values:", mixed_values)
print("List with positive values:", positive_values)
