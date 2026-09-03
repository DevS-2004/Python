# ================================================
#  Python Decorators Tutorial (Basic → Advanced)
# ================================================

from functools import wraps, lru_cache

# ------------------------------------------------
# 1. Basic idea: Functions are first-class citizens
# ------------------------------------------------
def greet(name):
    return f"Hello {name}"

say_hello = greet  # functions can be assigned to variables
print(say_hello("Ishu"))  # ✅ "Hello Ishu"


# ------------------------------------------------
# 2. Simple decorator (without @ syntax)
# ------------------------------------------------
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_hi():
    print("Hi!")

decorated = my_decorator(say_hi)
decorated()  # manually decorated


# ------------------------------------------------
# 3. Using @ syntax (cleaner)
# ------------------------------------------------
@my_decorator
def say_hello_world():
    print("Hello World!")

say_hello_world()


# ------------------------------------------------
# 4. Decorators with arguments (*args, **kwargs)
# ------------------------------------------------
def announce(func):
    def wrapper(*args, **kwargs):
        print("Function is starting...")
        result = func(*args, **kwargs)
        print("Function has ended.")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(3, 4))


# ------------------------------------------------
# 5. Preserving metadata with functools.wraps
# ------------------------------------------------
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

print(multiply(2, 5))
print(multiply.__name__)   # ✅ multiply
print(multiply.__doc__)    # ✅ "Multiplies two numbers"


# ------------------------------------------------
# 6. Decorators with parameters
# ------------------------------------------------
def log(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log("DEBUG")
def divide(a, b):
    return a / b

print(divide(10, 2))


# ------------------------------------------------
# 7. Chaining multiple decorators
# ------------------------------------------------
def bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet_html():
    return "Hello"

print(greet_html())  # <b><i>Hello</i></b>


# ------------------------------------------------
# 8. Real-world use cases
# ------------------------------------------------

# Logging
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def power(a, b):
    return a ** b

print(power(2, 5))

# Access Control (Authentication simulation)
def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            raise PermissionError("User not logged in ❌")
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def get_data(user):
    return f"Secret data for {user['name']}"

user = {"name": "Ishu", "logged_in": True}
print(get_data(user))


# Memoization (caching results)
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # efficient due to caching


# ------------------------------------------------
# 9. Class decorators
# ------------------------------------------------
def add_repr(cls):
    cls.__repr__ = lambda self: f"{cls.__name__}({self.__dict__})"
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

p = Person("Ishu", 21)
print(p)  # Person({'name': 'Ishu', 'age': 21})


# ------------------------------------------------
# 10. Advanced: Class as decorator
# ------------------------------------------------
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(3)
def hello():
    print("Hello!")

hello()  # prints "Hello!" 3 times
