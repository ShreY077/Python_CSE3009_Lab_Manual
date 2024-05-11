def verify_data(data):
    # Check if the data meets certain criteria (for example, it should not be empty)
    if data.strip():  # Check if the data contains non-space characters
        return True
    else:
        return False

def welcome_user(name):
    print("Welcome,", name, "!")

# Accept data from the user
data = input("Enter your name: ")

# Verify the data
if verify_data(data):
    # If the data is valid, print a welcome message
    welcome_user(data)
else:
    # If the data is invalid, print an error message
    print("Invalid input. Please enter your name.")
