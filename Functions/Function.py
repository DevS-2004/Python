# function_methods_demo.py
# Covers Python functions: creation, arguments, return values, scope, recursion,
# lambda, decorators, higher-order functions, and common pitfalls.
# Run this file to see examples and outputs directly in the console.

print("="*60)
print("1. Creating & Calling Functions")
print("="*60)

# Basic function
def greet(name):
    """Greets the user by name."""
    return f"Hello, {name}!"

print(greet("Ishu"))
print()

# --------------------------------------------------------
print("="*60)
print("2. Function Arguments")
print("="*60)

# Positional arguments
def add(a, b):
    return a + b
print("Positional:", add(2, 3))

# Keyword arguments
print("Keyword:", add(b=4, a=6))

# Default arguments
def power(base, exp=2):
    return base ** exp
print("Default exp=2:", power(5))
print("Override default:", power(5, 3))

# Variable-length (*args)
def sum_all(*numbers):
    print("args type:", type(numbers))
    return sum(numbers)
print("Sum all:", sum_all(1, 2, 3, 4))

# Variable-length (**kwargs)
def print_details(**info):
    print("kwargs type:", type(info))
    for k, v in info.items():
        print(f"{k} -> {v}")
print_details(name="Ishu", age=21, city="Kanpur")
print()

# --------------------------------------------------------
print("="*60)
print("3. Return Values")
print("="*60)

# Single value return
def square(n):
    return n * n
print("Square of 4:", square(4))

# Multiple values return (tuple packing/unpacking)
def calc(a, b):
    return a + b, a - b
add_res, sub_res = calc(5, 3)
print("Addition:", add_res, "Subtraction:", sub_res)
print()

# --------------------------------------------------------
print("="*60)
print("4. Scope: local, global, nonlocal")
print("="*60)

x = 10  # global variable

def local_scope():
    x = 5  # local variable
    print("Inside local_scope:", x)

def global_scope():
    global x
    x = 20
    print("Inside global_scope:", x)

def nonlocal_scope():
    def outer():
        y = "outer"
        def inner():
            nonlocal y
            y = "inner modified"
        inner()
        print("Inside outer after inner:", y)
    outer()

local_scope()
print("After local_scope, global x:", x)
global_scope()
print("After global_scope, global x:", x)
nonlocal_scope()
print()

# --------------------------------------------------------
print("="*60)
print("5. Lambda Functions (Anonymous)")
print("="*60)

square_lambda = lambda n: n * n
print("Lambda square of 4:", square_lambda(4))

add_lambda = lambda a, b: a + b
print("Lambda add:", add_lambda(3, 7))
print()

# --------------------------------------------------------
print("="*60)
print("6. Recursion")
print("="*60)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
print()

# --------------------------------------------------------
print("="*60)
print("7. Higher-Order Functions: map, filter, reduce")
print("="*60)

nums = [1, 2, 3, 4, 5]

# map
squares = list(map(lambda x: x * x, nums))
print("Squares via map:", squares)

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens via filter:", evens)

# reduce
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
print("Product via reduce:", product)
print()

# --------------------------------------------------------
print("="*60)
print("8. Decorators")
print("="*60)

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello from decorated function!")

say_hello()
print()

# --------------------------------------------------------
print("="*60)
print("9. Functions as First-Class Objects")
print("="*60)

def shout(text):
    return text.upper()

# Assigning to variable
yell = shout
print("Calling yell:", yell("hello"))

# Passing function as argument
def call_func(f, value):
    return f(value)
print("call_func:", call_func(shout, "ishu"))

# Returning a function from another function
def outer():
    def inner():
        return "Inner says hi"
    return inner

returned_func = outer()
print("Returned function call:", returned_func())
print()

# --------------------------------------------------------
print("="*60)
print("10. *args & **kwargs Pitfalls")
print("="*60)

def show_args(a, b, *args, **kwargs):
    print("a:", a, "b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

show_args(1, 2, 3, 4, x=5, y=6)
print()

# --------------------------------------------------------
print("="*60)
print("11. Common Misconceptions & Pitfalls")
print("="*60)

print("1) Default mutable arguments retain changes across calls:")

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print("Call 1:", append_to_list(1))
print("Call 2:", append_to_list(2), "<-- Unexpected!")
print("Solution: use None as default and handle inside.")

def append_safe(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print("Safe Call 1:", append_safe(1))
print("Safe Call 2:", append_safe(2))
print()

print("2) Functions without return return None by default.")

def no_return():
    pass

print("no_return() gives:", no_return())
print()

print("3) Functions are objects: can be stored in data structures.")

func_list = [shout, square]
for f in func_list:
    print(f"Calling {f.__name__}:", f(3) if f is square else f("test"))
