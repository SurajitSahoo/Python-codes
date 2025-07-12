#Set 3:
#1. Print the following pattern using loop for n no of rows
#1
#1 2
#1 2 3
#1 2 3 4

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
n = 4
print_pattern(n)