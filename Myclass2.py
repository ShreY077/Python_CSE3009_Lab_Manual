class MyClass:
    # Data member
    my_variable = "Hello, I'm a data member."

    # Function
    def my_function(self):
        return "Hello, I'm a function."

# Create an object of the class
obj = MyClass()

# Access the data member using the object
print("Data member:", obj.my_variable)

# Call the function using the object
print("Function:", obj.my_function())
