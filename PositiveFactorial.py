def factorial(num):
    # Check if the number is non-negative
    if num < 0:
        return "Factorial is not defined for negative numbers."
    # Calculate factorial
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Test the function
number = int(input("Enter a non-negative integer to calculate its factorial: "))
print("Factorial of", number, "is:", factorial(number))
