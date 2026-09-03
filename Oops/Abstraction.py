# Abstraction in Python
# ----------------------
# Abstraction is one of the four pillars of Object-Oriented Programming (OOP).
# It means hiding the internal implementation details and showing only the essential features of the object.
# The user interacts with only the necessary part without knowing the background complexity.
#
# Example in real life:
#   - When you use a TV remote, you only press buttons like "Power ON" or "Volume Up".
#   - You do not care about the internal electronic signals and circuits that make it work.
#   - That hidden internal process is "abstraction".
#
# In Python, abstraction is mostly achieved using:
#   - Abstract Classes
#   - Abstract Methods
#   - The "abc" module (Abstract Base Class)

from abc import ABC, abstractmethod

# ===========================================================
# Step 1: Create an abstract class
# ===========================================================
class Vehicle(ABC):   # ABC means Abstract Base Class
    @abstractmethod
    def start(self):
        pass   # Abstract method (must be implemented by child classes)

    @abstractmethod
    def stop(self):
        pass   # Abstract method (must be implemented by child classes)

    # ✅ Abstract classes CAN also have concrete methods
    def fuel_type(self):
        return "Generic fuel type: Petrol or Diesel"


# ===========================================================
# Step 2: Create concrete (child) classes that implement the abstract class
# ===========================================================
class Car(Vehicle):
    def start(self):
        return "Car has started with a key ignition."

    def stop(self):
        return "Car has stopped by turning off the key."

class Bike(Vehicle):
    def start(self):
        return "Bike has started with a self-start button."

    def stop(self):
        return "Bike has stopped with a side stand sensor."


# ===========================================================
# Step 3: Using abstraction
# ===========================================================
car = Car()
bike = Bike()

print("=== Abstraction Example ===")
print(car.start())
print(car.stop())
print(car.fuel_type())  # Calling concrete method from abstract class
print(bike.start())
print(bike.stop())


# ===========================================================
# Additional Example: Payment System
# ===========================================================
# Imagine a payment gateway system where abstraction is important.
# The user just selects the payment mode (CreditCard, PayPal, UPI),
# but does not know the internal validation steps.

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI."


print("\n=== Payment System Example (Abstraction) ===")
payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment3 = UPIPayment()

print(payment1.pay(500))
print(payment2.pay(1200))
print(payment3.pay(700))


# ===========================================================
# Pitfall Example: Not implementing abstract methods
# ===========================================================
class Truck(Vehicle):
    def start(self):
        return "Truck engine started."
    # ❌ Forgot to implement stop()

# Uncommenting this will throw error:
# truck = Truck()  # TypeError: Can't instantiate abstract class Truck with abstract method stop


# ===========================================================
# Key Points about Abstraction
# ===========================================================
# 1. Abstract classes cannot be instantiated directly:
#       v = Vehicle()  ❌ ERROR
#
# 2. Child classes must implement ALL abstract methods, otherwise they also become abstract
#    and cannot be instantiated.
#
# 3. Abstract classes can contain:
#       - Abstract methods (declared, no body)
#       - Concrete methods (fully defined, reusable by subclasses)
#
# 4. Abstraction helps reduce code complexity and increases reusability.
#
# 5. Abstract classes act as a CONTRACT:
#    - Any class that inherits from them MUST implement the required methods.


# ===========================================================
# Misconceptions about Abstraction
# ===========================================================
# ❌ Misconception 1: "Abstract methods are optional to implement."
# ✅ Wrong → They MUST be implemented in subclasses, otherwise subclass is abstract too.

# ❌ Misconception 2: "Abstract classes can’t have normal methods."
# ✅ Wrong → Abstract classes CAN have both abstract and concrete methods.

# ❌ Misconception 3: "We can create objects from abstract classes."
# ✅ Wrong → Abstract classes cannot be instantiated.

# ❌ Misconception 4: "If one method is missing, Python will ignore it."
# ✅ Wrong → Even a single unimplemented abstract method keeps the subclass abstract.


# ===========================================================
# Final Takeaway
# ===========================================================
# 🔹 Abstract classes are templates/blueprints.
# 🔹 They enforce rules for subclasses (must implement required methods).
# 🔹 They improve consistency across multiple implementations (e.g., Car, Bike, Truck must all have start() and stop()).
# 🔹 They provide both abstract and concrete behavior to subclasses.
