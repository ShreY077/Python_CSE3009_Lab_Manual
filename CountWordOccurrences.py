def count_word_occurrences(string):
    # Split the string into words
    words = string.split()

    # Create a dictionary to store word counts
    word_counts = {}

    # Count occurrences of each word
    for word in words:
        # Remove punctuation from the word
        word = word.strip(",.!?;:'\"").lower()
        # Update word count in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Test the function
string = input("Enter a string: ")
word_counts = count_word_occurrences(string)
print("Occurrences of each word:")
for word, count in word_counts.items():
    print(f"'{word}': {count}")
