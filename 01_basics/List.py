# list_methods_demo.py
# Covers Python list basics, methods, and common pitfalls
# Run this file to see examples and outputs directly in the console.

print("="*60)
print("1. Creating Lists & Basic Printing")
print("="*60)

# Basic list creation
nums = [1, 2, 3, 4]
print("nums =", nums)               # Prints the list directly
print("type(nums) =", type(nums))   # Lists are of type 'list'

# Empty list
empty = []
print("Empty list:", empty)

# Lists can contain mixed types (not recommended for strict data structures)
mixed = [1, "two", 3.0, True]
print("Mixed list:", mixed)
print()

# --------------------------------------------------------
print("="*60)
print("2. Taking Input into a List")
print("="*60)

# Example for integers from user (commented for demo)
# user_input = input("Enter numbers separated by space: ")
# nums_list = list(map(int, user_input.split()))  # split() same as in string
# print("List from input:", nums_list)

# Simulated example (hardcoded string)
nums_list = list(map(int, "10 20 30".split()))  # split() same as in string
print("List from input simulation:", nums_list)
print()

# --------------------------------------------------------
print("="*60)
print("3. Accessing Elements")
print("="*60)

lst = ["chai", "coffee", "milk"]
print("lst[0] ->", lst[0])      # First element (indexing same as in string)
print("lst[-1] ->", lst[-1])    # Negative indexing same as in string
print("lst[0:2] ->", lst[0:2])  # Slicing same as in string
print("lst[::-1] ->", lst[::-1])# Reverse slicing same as in string
print()

# --------------------------------------------------------
print("="*60)
print("4. Looping Over Lists")
print("="*60)

print("Using for loop (direct iteration over elements):")
for item in lst:
    print(item, end=" ")  # end parameter same as in print() for strings
print()

print("\nUsing index (less Pythonic, but sometimes needed):")
for i in range(len(lst)):  # len() same as in string
    print(f"Index {i} -> {lst[i]}")
print()

# --------------------------------------------------------
print("="*60)
print("5. Adding Elements")
print("="*60)

animals = ["cat", "dog"]

animals.append("cow")  # append() -> list-specific
print("append ->", animals)

animals.extend(["goat", "sheep"])  # extend() list-specific
print("extend ->", animals)

animals.insert(1, "tiger")  # insert() list-specific
print("insert ->", animals)
print()

# --------------------------------------------------------
print("="*60)
print("6. Removing Elements")
print("="*60)

fruits = ["apple", "banana", "mango", "banana"]

fruits.remove("banana")  # remove() list-specific
print("remove('banana') ->", fruits)

popped = fruits.pop()  # pop() also works in dict (removes by key there)
print("pop() removed ->", popped, "remaining:", fruits)

popped_index = fruits.pop(0)  # pop(index) list-specific
print("pop(0) removed ->", popped_index, "remaining:", fruits)

fruits.clear()  # clear() same as in dict & set
print("clear() ->", fruits)
print()

# --------------------------------------------------------
print("="*60)
print("7. Searching & Counting")
print("="*60)

colors = ["red", "blue", "green", "blue"]
print("colors.index('blue') ->", colors.index("blue"))  # index() same as in string
print("colors.count('blue') ->", colors.count("blue"))  # count() same as in string

# index() raises ValueError if not found (unlike find() in strings)
print("'yellow' in colors ->", "yellow" in colors)  # in operator same as in string, tuple, dict keys
print()

# --------------------------------------------------------
print("="*60)
print("8. Sorting & Reversing")
print("="*60)

nums = [5, 2, 9, 1]
nums.sort()  # sort() list-specific
print("sort() ->", nums)

nums.sort(reverse=True)  # sort(reverse=True) list-specific
print("sort(reverse=True) ->", nums)

nums = [5, 2, 9, 1]
print("sorted(nums) ->", sorted(nums), "original ->", nums)  # sorted() works with any iterable

nums.reverse()  # reverse() list-specific
print("reverse() ->", nums)
print()

# --------------------------------------------------------
print("="*60)
print("9. Copying Lists (Pitfall)")
print("="*60)

a = [1, 2, 3]
b = a  # Same reference (works like mutable types generally)
b.append(4)
print("a =", a, "b =", b)

a = [1, 2, 3]
b = a.copy()  # copy() same method name in dict & set
b.append(4)
print("a =", a, "b =", b)
print()

# --------------------------------------------------------
print("="*60)
print("10. List Comprehensions")
print("="*60)

squares = [x**2 for x in range(5)]
print("Squares ->", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares ->", even_squares)
print()

# --------------------------------------------------------
print("="*60)
print("11. Nested Lists (2D Lists)")
print("="*60)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("matrix[0][1] ->", matrix[0][1])  # Nested indexing same logic as in string of string
for row in matrix:
    print(row)
print()

# --------------------------------------------------------
print("="*60)
print("12. Built-in Functions with Lists")
print("="*60)

nums = [4, 2, 9, 1]
print("len(nums) ->", len(nums))  # len() same as in string
print("sum(nums) ->", sum(nums))  # sum() works for any numeric iterable
print("max(nums) ->", max(nums))  # max() works for any iterable
print("min(nums) ->", min(nums))  # min() works for any iterable
print()

# --------------------------------------------------------
print("="*60)
print("13. Common Misconceptions Recap")
print("="*60)

print("1) index() errors if item not found (check with 'in' first).")
print("2) remove() removes only the FIRST match, not all.")
print("3) sort() changes original list, sorted() returns new one.")
print("4) a = b makes them same object, use copy() to clone.")
print("5) list * n creates shallow copies of elements (see below).")

nested = [[0]] * 3
nested[0][0] = 99
l = [[1],2]*2
l[0][0] = 100
l[1] = 2000
print(l)  
print("nested ->", nested, "(all rows changed!)","It is because of shallow copy after multiplication.")
