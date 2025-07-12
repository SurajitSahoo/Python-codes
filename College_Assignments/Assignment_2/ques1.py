n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
    ave = sum/n
    print(f"The sum is:{sum}")
    print(f"The ave is:{ave}")