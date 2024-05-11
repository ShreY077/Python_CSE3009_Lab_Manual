from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class MyClass(Interface):
    def method1(self):
        return "Implementation of method1"

    def method2(self):
        return "Implementation of method2"

# Create an object of the subclass
obj = MyClass()
print(obj.method1())  # Output: Implementation of method1
print(obj.method2())  # Output: Implementation of method2
