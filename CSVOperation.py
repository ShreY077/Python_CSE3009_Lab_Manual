import csv

def write_csv_from_dict(filename, data):
    # Write data to a CSV file from a dictionary
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_csv_to_dict(filename):
    # Read data from a CSV file into a dictionary
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Test the functions
filename = "data.csv"

# Create data as a list of dictionaries
data_to_write = [
    {"Name": "John", "Age": 25, "City": "New York"},
    {"Name": "Alice", "Age": 30, "City": "Los Angeles"},
    {"Name": "Bob", "Age": 35, "City": "Chicago"},
    {"Name": "Emily", "Age": 40, "City": "Houston"},
    {"Name": "David", "Age": 45, "City": "Phoenix"}
]

# Write data to CSV file
write_csv_from_dict(filename, data_to_write)
print(f"Data written to '{filename}' successfully.")

# Read data from CSV file
data_read = read_csv_to_dict(filename)
print("Data read from CSV file:")
for row in data_read:
    print(row)
