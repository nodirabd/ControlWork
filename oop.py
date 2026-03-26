from abc import ABC, abstractmethod

#1 инкапсуляция
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age >=0:
            self.__age = age
        else:
            print(f'False. Write a valid age number')
    def get_age(self):
        return self.__age
print("1 инкапсуляция")

p1 = Person()
p1.set_age(47)
print(f'Age: {p1.get_age()}')
p1.set_age(-15)
print()

#2 наследование
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return 'I am an animal'
class Dog(Animal):
    def speak(self):
        return 'Woof'
class Cat(Animal):
    def speak(self):
        return 'Meow'
print("2 наследование")
dog = Dog('Sharik')
cat = Cat('Kissa')
print(dog.name, dog.speak())
print(cat.name, cat.speak())
print()

# 3 полиморфизм
class Vehicle():
    def move(self):
        return 'Vehicle is moving'
class Car(Vehicle):
    def move(self):
        return 'Car is driving'

class Bicycle(Vehicle):
    def move(self):
        return 'Bicycle is pedaling'


def move(vehicle):
    return vehicle.move()
print("3 Полиморфизм")
car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))
print()
#4 абстракция
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
print("4 абстракция")
rect = Rectangle(25, 5)
circle = Circle(4)
print(rect.area())
print(circle.area())
