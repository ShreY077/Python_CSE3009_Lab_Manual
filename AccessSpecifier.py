class MyClass:
    def __init__(self):
        # Public attribute
        self.public_attr = "I am a public attribute"
        # Protected attribute
        self._protected_attr = "I am a protected attribute"
        # Private attribute
        self.__private_attr = "I am a private attribute"

    def public_method(self):
        print("Public method called")
        # Accessing all attributes inside the class
        print("Accessing public attribute:", self.public_attr)
        print("Accessing protected attribute:", self._protected_attr)
        print("Accessing private attribute:", self.__private_attr)

    def _protected_method(self):
        print("Protected method called")

    def __private_method(self):
        print("Private method called")


# Create an object of the class
obj = MyClass()

# Accessing public attributes and methods
print("Accessing public attribute outside the class:", obj.public_attr)
obj.public_method()

# Accessing protected attributes and methods (conventionally)
print("Accessing protected attribute outside the class:", obj._protected_attr)
obj._protected_method()

# Accessing private attributes and methods (conventionally)
# Note: Accessing private attributes and methods directly outside the class may raise AttributeError
# print("Accessing private attribute outside the class:", obj.__private_attr)  # Raises AttributeError
# obj.__private_method()  # Raises AttributeError

# Accessing private attributes and methods using name mangling
print("Accessing private attribute outside the class:", obj._MyClass__private_attr)
obj._MyClass__private_method()
