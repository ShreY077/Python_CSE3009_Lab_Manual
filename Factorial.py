def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Get input from the user
number = int(input("Enter a number to find its factorial: "))

# Call the function to find factorial
result = factorial(number)

# Print the result
print("Factorial of", number, "is:", result)
