n = int(input("Enter a number: "))
for i in range(2,n):
    if(n%i == 0):
        print(f"The number {n} is not prime number")
    else:
        print(f"The number {n} is prime")    