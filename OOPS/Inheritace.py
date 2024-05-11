class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def sound(self):
        return "Woof!"

# Create an object of the subclass
dog = Dog("Buddy")
print(dog.species)  # Output: Dog
print(dog.sound())  # Output: Woof!
