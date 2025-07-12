# Function to count character occurrences in a file
def count_char_in_file(filename, char_to_count):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            return content.count(char_to_count)  # Return the count of the specified character
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

# Main program
if __name__ == "__main__":
    # Get the filename and character from the user
    filename = input("Enter the filename: ")
    char_to_count = input("Enter the character to count: ")

    if len(char_to_count) != 1:
        print("Please enter exactly one character to count.")
    else:
        # Count the character in the file
        count = count_char_in_file(filename, char_to_count)
        
        if count is not None:
            print(f"The character '{char_to_count}' appears {count} times in the file '{filename}'.")
