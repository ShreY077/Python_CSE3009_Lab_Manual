import pandas as pd

def create_csv_and_read():
    # Create a DataFrame
    data = {
        'Name': ['John', 'Alice', 'Bob', 'Emily', 'David'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    filename = "data.csv"
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' created successfully.")

    # Read the CSV file into a DataFrame
    df_read = pd.read_csv(filename)

    # Print the DataFrame
    print("Data read from CSV file:")
    print(df_read)

# Test the function
create_csv_and_read()
