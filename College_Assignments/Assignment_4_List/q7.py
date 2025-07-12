numbers = [4, 2, 5, 1, 3, 2, 5, 6]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_smallest = unique_numbers[1]
second_largest = unique_numbers[-2]

print("Second smallest:", second_smallest)  # Output: 2
print("Second largest:", second_largest)  # Output: 5
