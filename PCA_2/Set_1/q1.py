#1. WAP that creates a list of 10 random integers then creates 2 list- ODD list and EVEN list
#to store odd and even values 


import random

random_list = [random.randint(1, 100) for _ in range(10)]
odd_list = []
even_list = []

for num in random_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Random List:", random_list)
print("Odd List:", odd_list)
print("Even List:", even_list)
