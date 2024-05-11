try:
    # Prompt the user to input an integer
    num = int(input("Please enter an integer: "))
    print("You entered:", num)
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Please enter a valid integer.")
