n = int(input("Enter a number: "))
serise_sum = sum(1/i for i in range(1,n+1))
print(f"The sum of serise is: {serise_sum}")