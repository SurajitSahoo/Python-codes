number = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(number)))
print(f"The sum of the digits is: {digit_sum}")
