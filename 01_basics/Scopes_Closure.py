# =================================================
# SCOPES & CLOSURES IN PYTHON — COMPLETE GUIDE
# =================================================
# IMPORTANT RULES:
# 1. The 'global' and 'nonlocal' keywords only matter when used INSIDE a function.
#    - Outside any function, 'global' does nothing special because you're already in global scope.
#
# 2. 'nonlocal' can only be used inside a nested (inner) function to modify a variable
#    from its immediately enclosing function’s scope.
#    - If there’s no such enclosing function, 'nonlocal' will cause an error.
#
# LEGB Rule Recap:
#    L = Local       → Inside the current function 
#    E = Enclosing   → In outer functions (nonlocal)
#    G = Global      → Defined at module level or declared global
#    B = Built-in    → Preassigned names in Python (len, sum, etc.)
#
# Lookup order: Local → Enclosing → Global → Built-in
# =================================================


print("="*70)
print("1. Local vs Global Scope")
print("="*70)

name = "GlobalName"  # Global variable

def local_example():
    name = "LocalName"  # Local variable shadows global
    print("Inside local_example:", name)

def global_example():
    global name
    name = "ChangedGlobal"  # Modifies global variable
    print("Inside global_example:", name)

local_example()
print("After local_example:", name)
global_example()
print("After global_example:", name)
print()

# --------------------------------------------------------
print("="*70)
print("2. Nonlocal Scope")
print("="*70)

def outer_nonlocal():
    message = "Outer message"
    def inner():
        nonlocal message
        message = "Modified by inner"
        print("Inner sees:", message)
    inner()
    print("Outer sees after inner:", message)

outer_nonlocal()
print()

# --------------------------------------------------------
print("="*70)
print("3. Without vs With Nonlocal")
print("="*70)

def without_nonlocal():
    value = 100
    def inner():
        value = 200  # Creates a new local variable
        print("Inner value:", value)
    inner()
    print("Outer value:", value)

def with_nonlocal():
    value = 100
    def inner():
        nonlocal value
        value = 200  # Modifies outer function's variable
        print("Inner value:", value)
    inner()
    print("Outer value:", value)

print("-- Without nonlocal --")
without_nonlocal()
print("-- With nonlocal --")
with_nonlocal()
print()

# --------------------------------------------------------
print("="*70)
print("4. LEGB Rule Demonstration")
print("="*70)

x = "global X"
def outer():
    x = "enclosing X"
    def inner():
        x = "local X"
        print("Local wins:", x)
    inner()

outer()
print()

# --------------------------------------------------------
print("="*70)
print("5. Closure & Late Binding Problem")
print("="*70)

def closure_problem():
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)  # captures reference, not value
    return funcs

print("Closure problem:", [f() for f in closure_problem()], "<-- All same due to late binding")

def closure_solution():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)  # default captures current value
    return funcs

print("Closure fixed:", [f() for f in closure_solution()])
print()

# --------------------------------------------------------
print("="*70)
print("6. Common Pitfalls & Misconceptions")
print("="*70)

print("1) 'nonlocal' only works with variables in the nearest enclosing function.")
print("   It cannot reach directly into global scope — use 'global' for that.\n")

print("2) Mutable default arguments retain changes across calls:")

def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print("Call 1:", add_item("apple"))
print("Call 2:", add_item("banana"), "<-- Unexpected shared list!")

print("\n   Fix: Use None and create new list inside.")

def add_item_safe(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print("Safe Call 1:", add_item_safe("apple"))
print("Safe Call 2:", add_item_safe("banana"))
print()

# --------------------------------------------------------
print("="*70)
print("7. Tricky Questions for Practice")
print("="*70)

print("Q1: What will this print?")
def tricky1():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

inc_func = tricky1()
print("Increment calls:", inc_func(), inc_func(), inc_func())

print("\nQ2: Late binding test")
funcs = [lambda: n for n in range(4)]
print("Late binding:", [f() for f in funcs])

funcs_fixed = [lambda n=n: n for n in range(4)]
print("Fixed binding:", [f() for f in funcs_fixed])

print("\nQ3: Global variable change inside a function:")
y = 50
def change_global():
    global y
    y = 99
change_global()
print("y after function:", y)

print("\nQ4: Nonlocal can't modify global — True or False?")
print("True. 'nonlocal' only touches enclosing functions' variables.")

# --------------------------------------------------------
print("="*70)
print("8. Closure Example")
print("="*70)

def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times3 = make_multiplier(3)
print("3 * 5 =", times3(5))
print("3 * 10 =", times3(10))
