def multiply(n):
    for i in range(1, n+1):
        print(f"{n} X {i} = {n*i}")
n = int(input("Enter a number: "))
print(multiply(n))        