def divide():
    try:
        x = float(input("Enter the numerator: "))
        y = float(input("Enter the denominator: "))
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Result of division:", result)
    finally:
        print("Executing finally block")

# Call the function
divide()
