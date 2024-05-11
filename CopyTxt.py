import os

def copy_file(source_file, destination_file):
    # Open the source file for reading
    with open(source_file, 'r') as source:
        # Read the content of the source file
        content = source.read()
    # Open the destination file for writing
    with open(destination_file, 'w') as destination:
        # Write the content to the destination file
        destination.write(content)
    print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")

# Source file
source_file = "sample.txt"  # Replace with the path to your source file

# Destination file in the specified directory
destination_file = "destination.txt"  # Replace with the name of your destination file
destination_path = os.path.join(destination_file)

# Copy the contents of the source file to the destination file
copy_file(source_file, destination_path)
