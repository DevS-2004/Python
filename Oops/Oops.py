# =================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON — COMPLETE GUIDE
# =================================================
# Key Pillars of OOP:
# 1. Encapsulation   → Bundle data (attributes) & behavior (methods) into objects.
# 2. Abstraction     → Hide implementation details, show only relevant interface.
# 3. Inheritance     → Create new classes from existing ones (reuse & extend code).
# 4. Polymorphism    → Same interface, different implementation.
#
# Special Python Features:
# - __init__       → Constructor
# - self           → Reference to current object
# - @classmethod   → Method bound to class, not instance
# - @staticmethod  → Method bound to neither instance nor class
# - __str__, __repr__ → Object string representation
# =================================================


print("=" * 70)
print("1. Class & Object Basics")
print("=" * 70)

class Person:
    def __init__(self, name, age):
        self.name = name        # Instance attribute
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 30)
p1.greet()
print()


# --------------------------------------------------------
print("=" * 70)
print("2. Encapsulation")
print("=" * 70)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (name-mangled)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Bob", 1000)
account.deposit(500)
print("Balance after deposit:", account.get_balance())
# account.__balance  # ❌ AttributeError
print()


# --------------------------------------------------------
print("=" * 70)
print("3. Inheritance")
print("=" * 70)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

for creature in (a, d, c):
    creature.speak()
print()


# --------------------------------------------------------
print("=" * 70)
print("4. Polymorphism")
print("=" * 70)

def make_it_speak(animal):
    animal.speak()

make_it_speak(Dog())
make_it_speak(Cat())
print()


# --------------------------------------------------------
print("=" * 70)
print("5. Class Methods & Static Methods")
print("=" * 70)

class MyClass:
    class_var = 0

    def __init__(self):
        MyClass.class_var += 1

    @classmethod
    def get_class_var(cls):
        return cls.class_var

    @staticmethod
    def say_hello():
        print("Hello from static method!")

obj1 = MyClass()
obj2 = MyClass()
print("Class var count:", MyClass.get_class_var())
MyClass.say_hello()
print()


# --------------------------------------------------------
print("=" * 70)
print("6. Dunder Methods (__str__, __repr__)")
print("=" * 70)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

b = Book("1984", "George Orwell")
print("Using __str__:", str(b))
print("Using __repr__:", repr(b))
print()


# --------------------------------------------------------
print("=" * 70)
print("7. Multiple Inheritance & MRO (Method Resolution Order)")
print("=" * 70)

class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")

class C(A):
    def process(self):
        print("C process")

class D(B, C):
    pass

d = D()
d.process()  # Uses B's process (MRO: D -> B -> C -> A)
print("MRO:", D.mro())
print()


# --------------------------------------------------------
print("=" * 70)
print("8. Abstract Classes")
print("=" * 70)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

rect = Rectangle(4, 5)
print("Rectangle area:", rect.area())
print()


# --------------------------------------------------------
print("=" * 70)
print("9. Common Pitfalls & Notes")
print("=" * 70)

print("1) In Python, 'private' is by convention (__var), but can still be accessed via name mangling.")
print("2) Multiple inheritance can cause ambiguity — check MRO carefully.")
print("3) Avoid mutable default arguments in __init__ to prevent shared state between instances.\n")


# --------------------------------------------------------
print("=" * 70)
print("10. Practice Questions")
print("=" * 70)

print("Q1: Create a class Car with attributes make, model, and year, and a method display_info().")
print("Q2: Implement a base class Employee and subclasses Manager and Developer with different work() methods.")
print("Q3: Write a class Counter that tracks number of instances created using a class variable.")
print("Q4: Create an abstract class Shape with abstract methods area() and perimeter(). Implement Circle and Rectangle.")
print("Q5: Demonstrate polymorphism using different shapes and a common method get_area().")
