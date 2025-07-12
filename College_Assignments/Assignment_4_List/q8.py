from collections import Counter

# Open and read the file
with open('your_file.txt', 'r') as file:
    data = file.read().split()

# Count the frequency of each element
frequency = Counter(data)

# Print the frequency of each element
for word, count in frequency.items():
    print(f"{word}: {count}")
