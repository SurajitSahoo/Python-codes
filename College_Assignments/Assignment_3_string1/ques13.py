def find_non_repeating_characters(input_string):
    non_repeating_chars = [char for char in input_string if input_string.count(char) == 1]
    print(*non_repeating_chars)

user_input = input("Enter a string: ")
find_non_repeating_characters(user_input)
