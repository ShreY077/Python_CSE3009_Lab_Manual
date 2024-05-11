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

# Function to delete from table
def delete_from_table(connection):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM example_table WHERE name = %s"
        val = ("John",)
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted.")
        print_table(connection)
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
        delete_from_table(connection)
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
