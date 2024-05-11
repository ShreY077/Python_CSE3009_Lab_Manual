def read_first_n_lines(filename, n):
    lines = []
    # Open the file
    with open(filename, 'r') as file:
        # Read the first n lines
        for _ in range(n):
            line = file.readline()
            if not line:  # If end of file is reached
                break
            lines.append(line.strip())  # Remove newline character and add to list
    return lines

# Test the function
filename = "sample.txt"  # Replace with the path to your text file
n = 3  # Number of lines to read
first_n_lines = read_first_n_lines(filename, n)

print(f"First {n} lines of '{filename}':")
for line in first_n_lines:
    print(line)
