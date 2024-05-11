from collections import Counter

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")

def count_most_frequent_words(filename, num_words=5):
    # Read the text from the file
    with open(filename, 'r') as file:
        text = file.read()

    # Tokenize the text into words
    words = text.split()

    # Count the frequency of each word
    word_freq = Counter(words)

    # Find the most frequent words
    most_common_words = word_freq.most_common(num_words)

    return most_common_words

# Create a text file and add some content to it
filename = "sample.txt"
content = "apple banana banana cherry cherry cherry cherry cherry"
create_file(filename, content)

# Count the most frequent words from the file
num_words = 3  # Number of most frequent words to find
most_frequent_words = count_most_frequent_words(filename, num_words)

print("Most frequent words:")
for word, frequency in most_frequent_words:
    print(f"{word}: {frequency}")
