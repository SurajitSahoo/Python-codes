#2. WAP to create a list of nos in the specified range in particular steps. Reverse the list and print its value


start = 1
end = 20
step = 2

number_list = list(range(start, end, step))
reversed_list = number_list[::-1]
print("Original list:", number_list)
print("Reversed list:", reversed_list)
