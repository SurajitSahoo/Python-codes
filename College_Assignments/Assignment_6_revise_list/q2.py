import random

# Create a list of 10 random integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]

# Initialize two empty lists: one for even numbers, one for odd numbers
even_list = []
odd_list = []

# Iterate over the random list and separate odd and even numbers
for number in random_list:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

# Print the random list, even list, and odd list
print("Random List:", random_list)
print("Even List:", even_list)
print("Odd List:", odd_list)
