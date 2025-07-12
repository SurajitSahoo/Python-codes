def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(f"{s} -> The string is a palindrome.")
    print(f"{s[::-1]}")
else:
    print(f"{s} -> The string is not a palindrome.")
    print(f"{s[::-1]}")

is_palindrome(s)