from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

# Create an object of the subclass
dog = Dog()
print(dog.sound())  # Output: Woof!
