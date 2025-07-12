def calculate_vowel_consonant_percentage(filename):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            total_chars = sum(1 for char in content if char.isalpha())
            vowels_count = sum(1 for char in content if char in vowels)
            consonants_count = total_chars - vowels_count

            if total_chars > 0:
                print(f"Vowels: {vowels_count/total_chars*100:.2f}%")
                print(f"Consonants: {consonants_count/total_chars*100:.2f}%")
            else:
                print("No alphabetic characters found.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Main
filename = input("Enter filename: ")
calculate_vowel_consonant_percentage(filename)
