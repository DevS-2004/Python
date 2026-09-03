# Private Public Protected -> Is just a convention in Python
# Python does not enforce access restrictions like some other languages.
# Instead, it uses naming conventions to indicate the intended access level.
# In this example, we will demonstrate the use of public, protected, and private attributes/methods in a class.


class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name          # Public attribute
        self._balance = balance   # Protected attribute (by convention)
        self.__pin = pin          # Private attribute (name mangled)

    # Public method: accessible everywhere
    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self._balance}")   # can access protected inside

    # Public method that uses private internally
    def verify_pin(self, pin):
        if self.__pin == pin:
            return "PIN Verified ✅"
        else:
            return "Wrong PIN ❌"

    # Protected method: intended for subclasses
    def _deduct_money(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    # Private method: strict internal use
    def __reset_pin(self, new_pin):
        self.__pin = new_pin
        return "PIN changed successfully!"


# Subclass example
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # Accessing protected member (_balance) is okay inside subclass
        if self._deduct_money(amount):
            print(f"Withdrawal successful! Remaining Balance: ₹{self._balance}")
        else:
            print("Insufficient funds ❌")


# ------------ Demo ------------

acc = SavingsAccount("Ishu", 5000, 1234)

# 1. Public access (allowed)
print(acc.name)            # ✅ works (public)
acc.show_details()         # ✅ works (public method)

# 2. Protected access (possible, but discouraged)
print(acc._balance)        # ⚠️ works, but should be avoided outside class
acc.withdraw(1500)         # ✅ subclass can use protected method

# 3. Private access (direct access not possible)
# print(acc.__pin)         # ❌ AttributeError
print(acc.verify_pin(1234)) # ✅ safe way to check private data

# 4. But you *can* hack into private using name-mangling
print(acc._BankAccount__pin)  # ⚠️ works, but bad practice
