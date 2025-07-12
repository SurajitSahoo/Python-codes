# Create a set of even numbers in the range 1-10
even_numbers = {num for num in range(1, 11) if num % 2 == 0}

# Create a set of composite numbers in the range 1-20
composite_numbers = {num for num in range(1, 21) if num > 1 and any(num % i == 0 for i in range(2, num))}

# Demonstrating use of all() on even numbers set
# all() checks if all elements in the iterable are True (or satisfy the condition)
are_all_even = all(num % 2 == 0 for num in even_numbers)

# Demonstrating use of issuperset() - Check if even_numbers is a superset of composite_numbers
is_even_superset = even_numbers.issuperset(composite_numbers)

# Demonstrating use of len() - Find the length of both sets
even_length = len(even_numbers)
composite_length = len(composite_numbers)

# Demonstrating use of sum() - Sum of all elements in both sets
even_sum = sum(even_numbers)
composite_sum = sum(composite_numbers)

# Output results
print("Even Numbers Set:", even_numbers)
print("Composite Numbers Set:", composite_numbers)
print(f"Are all numbers in the even numbers set even? {are_all_even}")
print(f"Is the even numbers set a superset of the composite numbers set? {is_even_superset}")
print(f"Length of Even Numbers Set: {even_length}")
print(f"Length of Composite Numbers Set: {composite_length}")
print(f"Sum of Even Numbers Set: {even_sum}")
print(f"Sum of Composite Numbers Set: {composite_sum}")
