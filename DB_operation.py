import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  #your DB password
            database=""   #your DB name 
        )
        print("Connected to MySQL database successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to create table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS example_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
        print("Table created successfully.")
        print_table(connection)
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to alter table
def alter_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE example_table ADD COLUMN email VARCHAR(255)")
        print("Table altered successfully.")
        print_table(connection)
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to insert into table
def insert_into_table(connection):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO example_table (name, age, email) VALUES (%s, %s, %s)"
        val = [("John", 30, "john@example.com"), ("Alice", 25, "alice@example.com"), ("Bob", 35, "bob@example.com")]
        cursor.executemany(sql, val)
        connection.commit()
        print(cursor.rowcount, "record(s) inserted.")
        print_table(connection)
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to update table
def update_table(connection):
    try:
        cursor = connection.cursor()
        sql = "UPDATE example_table SET age = %s WHERE name = %s"
        val = (40, "John")
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "record(s) updated.")
        print_table(connection)
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to drop table
def drop_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS example_table")
        print("Table dropped successfully.")
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to print table contents
def print_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM example_table")
        result = cursor.fetchall()
        print("Table contents:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Main function
def main():
    connection = connect_to_mysql()
    if connection:
        create_table(connection)
        alter_table(connection)
        insert_into_table(connection)
        update_table(connection)
        drop_table(connection)
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
