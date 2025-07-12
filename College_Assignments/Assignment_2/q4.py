n = int(input("Enter the number: "))
digit_sum = sum(int(digit) for digit in str(abs(n)))
print(f"the sum of the digit is: {digit_sum}")