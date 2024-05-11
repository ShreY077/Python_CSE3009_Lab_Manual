def search_string_in_file(filename, search_string):
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read each line in the file
        for line_number, line in enumerate(file, start=1):
            # Check if the search string is in the current line
            if search_string in line:
                print(f"Found '{search_string}' in '{filename}' at line {line_number}:")
                print(line.strip())

# Test the function
filename = "sample.txt"  # Replace with the path to your text file
search_string = "apple"  # The string to search for
search_string_in_file(filename, search_string)
