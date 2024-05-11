def reverse_string(string):
    # Use string slicing to reverse the string
    reversed_string = string[::-1]
    return reversed_string

# Test the function
sample_string = "1234abcd"
reversed_output = reverse_string(sample_string)
print("Original string:", sample_string)
print("Reversed string:", reversed_output)
