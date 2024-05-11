def remove_odd_index_characters(string):
    # Initialize an empty string to store characters with even indices
    result = ""

    # Iterate through the characters of the string
    for index, char in enumerate(string):
        # Check if the index is even
        if index % 2 == 0:
            # Append the character to the result string
            result += char

    return result

# Test the function
given_string = input("Enter a string: ")
result_string = remove_odd_index_characters(given_string)
print("Result string:", result_string)
