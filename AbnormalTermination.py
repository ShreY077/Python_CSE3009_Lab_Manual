import sys

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
        sys.exit(1)  # Abnormal termination with exit code 1
    else:
        print("Result of division:", result)

# Test cases
divide(10, 2)  # Output: Result of division: 5.0
divide(10, 0)  # Output: Error: Division by zero!
