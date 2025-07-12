# Create set 'sequences' containing numbers 1 to 10
sequences = {num for num in range(1, 11)}

# Create set 'cubes' containing cubes of numbers 1 to 10
cubes = {num**3 for num in range(1, 11)}

# Demonstrating the use of update() - adding elements from cubes to sequences
sequences.update(cubes)

# Demonstrating the use of pop() - removing and returning an arbitrary element from sequences
popped_element = sequences.pop()

# Demonstrating the use of add() - adding a new element (0) to sequences
sequences.add(0)

# Demonstrating the use of clear() - clearing all elements from cubes
cubes.clear()

# Output the results
print("Updated Sequences Set:", sequences)
print("Popped Element:", popped_element)
print("Cubes Set after clear():", cubes)
