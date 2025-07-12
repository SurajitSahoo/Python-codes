def hfc(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    max_char = max(char_count, key=char_count.get)
    
    print(f"The character with the highest frequency in the string is: {max_char}")
user_input = input("Enter a string: ")
hfc(user_input)
