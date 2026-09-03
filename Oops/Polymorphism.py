# =====================================
# Polymorphism in Python
# =====================================
# Polymorphism means "many forms".
# In Object-Oriented Programming (OOP), it allows different classes
# to define methods with the same name but behave differently.
# 
# Example: Different animals make different sounds,
# but all use the same method name 'speak'.

# -------------------------------------
# Example 1: Polymorphism with Methods
# -------------------------------------
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# Function using polymorphism
def animal_sound(animal):
    # Calls 'speak()' method no matter which class object is passed
    print(animal.speak())


# -------------------------------------
# Example 2: Polymorphism with Inheritance
# -------------------------------------
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly, but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

# -------------------------------------
# Example 3: Polymorphism with Functions
# -------------------------------------
# In Python, polymorphism also applies to built-in functions
# like len(), which works for different data types.

def polymorphism_with_builtin():
    print(len("OpenAI"))         # String -> 6
    print(len([10, 20, 30]))     # List -> 3
    print(len({"a": 1, "b": 2})) # Dictionary -> 2


# -------------------------------------
# Example 4: Operator Overloading (Polymorphism in Operators)
# -------------------------------------
# Operators like + behave differently based on the data types.

def operator_overloading():
    print(10 + 20)        # Adds integers -> 30
    print("Hello " + "World")  # Concatenates strings -> "Hello World"
    print([1, 2] + [3, 4])     # Merges lists -> [1, 2, 3, 4]


# -------------------------------------
# Example 5: Method Overloading (Not directly supported in Python)
# -------------------------------------
# Python does not support traditional method overloading
# (like Java or C++), but we can achieve similar behavior
# using default arguments or *args.

class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c


# -------------------------------------
# Example 6: Method Overriding
# -------------------------------------
# Method overriding is runtime polymorphism.
# A child class can override the method of the parent class.

class Vehicle:
    def fuel_type(self):
        return "Diesel or Petrol"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric Charge"


# =====================================
# MAIN EXECUTION
# =====================================
if __name__ == "__main__":

    print("---- Example 1: Method Polymorphism ----")
    dog = Dog()
    cat = Cat()
    cow = Cow()
    animal_sound(dog)
    animal_sound(cat)
    animal_sound(cow)

    print("\n---- Example 2: Inheritance Polymorphism ----")
    bird = Bird()
    sparrow = Sparrow()
    ostrich = Ostrich()
    bird.intro()
    bird.flight()
    sparrow.flight()
    ostrich.flight()

    print("\n---- Example 3: Built-in Function Polymorphism ----")
    polymorphism_with_builtin()

    print("\n---- Example 4: Operator Overloading ----")
    operator_overloading()

    print("\n---- Example 5: Method Overloading Simulation ----")
    m = Math()
    print(m.add())           # 0
    print(m.add(5, 10))      # 15
    print(m.add(1, 2, 3))    # 6

    print("\n---- Example 6: Method Overriding ----")
    v = Vehicle()
    e = ElectricCar()
    print("Vehicle fuel:", v.fuel_type())
    print("ElectricCar fuel:", e.fuel_type())
