s = int(input("Enter a string: "))
a = s[::-1]
if(s==s[::-1]):
    print("This is palindrome")
    print(f"{a}")
else:
    print("This is not palindrome")
    print(f"{a}")    