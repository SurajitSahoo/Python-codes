string = input("Enter a string: ")
vowels = "aeiou"
for char in string:
    if char in vowels:
        upper_char = char.upper()
        string = string.replace(char, upper_char)
print("Updated string:", string)
