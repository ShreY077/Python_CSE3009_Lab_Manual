class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

# Create an object of the subclass
dog = Dog()
print(dog.sound())  # Output: Woof!
