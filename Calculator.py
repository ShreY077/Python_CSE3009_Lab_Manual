def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def menu():
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Get user input for operation choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform operation based on user's choice
if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", addition(num1, num2))
    elif choice == '2':
        print("Result:", subtraction(num1, num2))
    elif choice == '3':
        print("Result:", multiplication(num1, num2))
    elif choice == '4':
        print("Result:", division(num1, num2))
else:
    print("Invalid choice. Please enter a valid option (1/2/3/4).")

