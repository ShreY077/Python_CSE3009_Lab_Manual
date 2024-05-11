import re

def validate_password(password):
    # Define the regular expressions for each criteria
    regex_lowercase = re.compile(r'[a-z]')
    regex_uppercase = re.compile(r'[A-Z]')
    regex_digit = re.compile(r'[0-9]')
    regex_special = re.compile(r'[$#@]')
    
    # Check the length of the password
    if len(password) < 6 or len(password) > 16:
        return False, "Password length should be between 6 and 16 characters."
    
    # Check if the password meets all criteria using regular expressions
    if (not regex_lowercase.search(password) or
        not regex_uppercase.search(password) or
        not regex_digit.search(password) or
        not regex_special.search(password)):
        return False, ("Password must contain at least one lowercase letter, one uppercase letter, "
                       "one digit, and one special character ($#@).")
    
    # Password meets all criteria
    return True, "Password is valid."

# Test the function
password = input("Enter a password to validate: ")
is_valid, message = validate_password(password)
print(message)
