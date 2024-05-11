def key_exists(dictionary, key):
    # Check if the key exists using the 'in' operator
    if key in dictionary:
        return True, dictionary[key]  # Return True and corresponding value
    else:
        return False, None  # Return False and None for the value

# Test the function
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

key_to_check = input("Enter the key to check: ")

exists, value = key_exists(my_dict, key_to_check)

if exists:
    print(f"The key '{key_to_check}' exists in the dictionary with value '{value}'.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
