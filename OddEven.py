def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

# Test the function
number = int(input("Enter a number: "))
check_even_odd(number)
