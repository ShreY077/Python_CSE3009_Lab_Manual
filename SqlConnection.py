import mysql.connector

def connect_to_mysql(host, user, password, database):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'  # Specify the authentication plugin
        )
        print("Connected to MySQL database successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Test the function
host = "localhost"  # Hostname of the MySQL server
user = "root"    # MySQL username
password = "Shreyansh7"  # MySQL password
database = "exampledb"  # Name of the database you want to connect to

connection = connect_to_mysql(host, user, password, database)
