# Class and Object
# A class is a blueprint for creating objects.

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Pranavi")
s.display()


# Constructor
# __init__() is automatically called when an object is created.

class Employee:
    def __init__(self, name):
        self.name = name

emp = Employee("Alice")
print(emp.name)


# Instance Variable
# Variables that belong to each object separately.

class Car:
    def __init__(self, brand):
        self.brand = brand

car = Car("BMW")
print(car.brand)


# Class Variable
# Variable shared by all objects of a class.

class Company:
    company = "Google"

    def __init__(self, name):
        self.name = name

c1 = Company("Alice")
c2 = Company("Bob")

print(c1.company)
print(c2.company)


# Instance Method
# Works with object data using the self parameter.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("Pranavi")
p.greet()


# Class Method
# Uses cls to access or modify class variables.

class College:
    college = "ABC"

    @classmethod
    def change_college(cls, name):
        cls.college = name

College.change_college("XYZ")
print(College.college)


# Static Method
# Independent of both object and class variables.

class Math:

    @staticmethod
    def square(x):
        return x * x

print(Math.square(5))


# Single Inheritance
# One child class inherits from one parent class.

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()


# Multilevel Inheritance
# A child class inherits from another child class.

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()


# Multiple Inheritance
# A class inherits from more than one parent.

class Father:
    def money(self):
        print("Money")

class Mother:
    def care(self):
        print("Care")

class Child(Father, Mother):
    pass

c = Child()
c.money()
c.care()


# Hierarchical Inheritance
# Multiple child classes inherit from one parent.

class Vehicle:
    def start(self):
        print("Started")

class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass

Bike().start()
Car().start()


# Method Overriding
# Child class provides its own implementation of a parent method.

class Bird:
    def fly(self):
        print("Bird flies")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

Sparrow().fly()


# Method Overloading
# Python achieves it using default or variable arguments.

class Calculator:
    def add(self, a, b=0):
        return a + b

cal = Calculator()
print(cal.add(5))
print(cal.add(5, 10))


# Encapsulation
# Hides data using private variables.

class Bank:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())


# Abstraction
# Hides implementation details using abstract classes.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Square(4).area())


# super()
# Calls the parent class constructor or methods.

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

Child()


# isinstance()
# Checks whether an object belongs to a class.

print(isinstance(d, Dog))
print(isinstance(d, Animal))


# issubclass()
# Checks whether one class inherits from another.

print(issubclass(Dog, Animal))


# Magic Method (__str__)
# Controls how an object is printed.

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

print(Book("Python"))


# Operator Overloading
# Allows operators like + to work with user-defined objects.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


# Property Decorator
# Access a method like an attribute.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)