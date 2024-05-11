class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic function
def make_sound(animal):
    return animal.speak()

# Test the polymorphic function
dog = Dog()
cat = Cat()
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!
