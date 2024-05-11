import sys

def word_count(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    # Count the number of words
    return len(words)

# Check if the program is run with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python program_name.py 'sentence'")
    sys.exit(1)

# Get the sentence from the command-line argument
sentence = sys.argv[1]

# Calculate and print the word count
count = word_count(sentence)
print("Word count:", count)
