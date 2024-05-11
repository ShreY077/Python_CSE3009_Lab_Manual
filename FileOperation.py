import os

# Specify the full path to the file in the desired directory
directory = "C:\\Users\\ASUS\\Desktop\\Python Practicals"
filename = os.path.join(directory, "sample.txt")

# i) Create a text file
def create_file(filename):
    try:
        with open(filename, 'x'):
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"Error: File '{filename}' already exists.")

# ii) Open a text file
def open_file(filename, mode='r'):
    try:
        file = open(filename, mode)
        print(f"File '{filename}' opened successfully.")
        return file
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# iii) Read from a text file
def read_file(file):
    if file:
        content = file.read()
        print("File content:")
        print(content)
        file.close()  # Close the file after reading its content

# iv) Write to a text file
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"Content written to file '{filename}' successfully.")

# v) Append to a text file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
        print(f"Content appended to file '{filename}' successfully.")

# vi) Close a text file
# Since files are opened using 'with' statement, they are automatically closed

# vii) Delete a text file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Test the functions
create_file(filename)
file = open_file(filename)
read_file(file)
write_to_file(filename, "Hello, world!\n")
file = open_file(filename)
read_file(file)
append_to_file(filename, "This is a new line.\n")
file = open_file(filename)
read_file(file)
delete_file(filename)
