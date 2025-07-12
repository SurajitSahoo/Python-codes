def count_characters():
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    while True:
        char = input("Enter a character (or * to stop): ")

        if char == '*':
            break

        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    print(f"Uppercase count: {uppercase_count}")
    print(f"Lowercase count: {lowercase_count}")
    print(f"Digit count: {digit_count}")

count_characters()
