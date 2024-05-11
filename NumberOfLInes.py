from collections import Counter

def count_lines(filename):
    # Open the file and read lines
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Count the number of lines
    num_lines = len(lines)
    return num_lines

def count_word_frequency(filename):
    # Open the file and read content
    with open(filename, 'r') as file:
        content = file.read()
    # Tokenize the content into words
    words = content.split()
    # Count the frequency of each word
    word_freq = Counter(words)
    return word_freq

# Test the functions
filename = "sample.txt"  # Replace with the path to your text file
num_lines = count_lines(filename)
print(f"Number of lines in '{filename}': {num_lines}")

word_freq = count_word_frequency(filename)
print("Word frequencies:")
for word, frequency in word_freq.items():
    print(f"{word}: {frequency}")
