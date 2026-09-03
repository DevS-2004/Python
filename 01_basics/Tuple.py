# tuple_methods_demo.py
# Covers Python tuple basics, methods, and common pitfalls
# Run this file to see examples and outputs directly in the console.

print("="*60)
print("1. Creating Tuples & Basic Printing")
print("="*60)

# Basic tuple creation
tup = (1, 2, 3, 4)
print("tup =", tup)
print("type(tup) =", type(tup))   # Tuples are of type 'tuple'

# Empty tuple
empty = ()
print("Empty tuple:", empty)

# Tuples can contain mixed types
mixed = (1, "two", 3.0, True)
print("Mixed tuple:", mixed)
print()

# --------------------------------------------------------
print("="*60)
print("2. Creating Tuples without Parentheses")
print("="*60)

tup2 = 5, 10, 15   # Parentheses optional in many cases
print("tup2 =", tup2, "type =", type(tup2))

# IMPORTANT: Single-element tuple must have a trailing comma
single = (42,)
print("Single-element tuple:", single, "type =", type(single))

not_tuple = (42)
print("Without comma:", not_tuple, "type =", type(not_tuple))
print()

# --------------------------------------------------------
print("="*60)
print("3. Accessing Elements")
print("="*60)

tup = ("chai", "coffee", "milk")
print("tup[0] ->", tup[0])      # First element
print("tup[-1] ->", tup[-1])    # Last element
print("tup[0:2] ->", tup[0:2])  # Slicing
print("tup[::-1] ->", tup[::-1])# Reverse slicing
print()

# --------------------------------------------------------
print("="*60)
print("4. Looping Over Tuples")
print("="*60)

print("Using for loop:")
for item in tup:
    print(item, end=" ")
print()

print("\nUsing index:")
for i in range(len(tup)):
    print(f"Index {i} -> {tup[i]}")
print()

# --------------------------------------------------------
print("="*60)
print("5. Tuple Immutability")
print("="*60)

tup = (1, 2, 3)
# tup[0] = 10  # ❌ Uncommenting will cause TypeError
print("Tuples cannot be modified after creation.")

# But if tuple contains mutable elements, those can be changed
tup_with_list = (1, [2, 3], 4)
tup_with_list[1][0] = 99
print("Mutable element changed inside tuple ->", tup_with_list)
print()

# --------------------------------------------------------
print("="*60)
print("6. Adding & Removing Elements (Trick)")
print("="*60)

tup1 = (1, 2)
tup2 = (3, 4)

# Adding tuples means concatenation
tup3 = tup1 + tup2
print("Concatenation ->", tup3)

# Repetition
tup4 = tup1 * 3
print("Repetition ->", tup4)

# No remove() or append() in tuple
# Need to convert to list first
tup_list = list(tup1)
tup_list.append(5)
tup1 = tuple(tup_list)
print("After append via list ->", tup1)
print()

# --------------------------------------------------------
print("="*60)
print("7. Searching & Counting")
print("="*60)

colors = ("red", "blue", "green", "blue")
print("colors.index('blue') ->", colors.index("blue"))  # First occurrence
print("colors.count('blue') ->", colors.count("blue"))

print("'yellow' in colors ->", "yellow" in colors)
print()

# --------------------------------------------------------
print("="*60)
print("8. Tuple Packing & Unpacking")
print("="*60)

packed = "apple", "banana", "cherry"  # Packing
print("packed tuple ->", packed)

a, b, c = packed  # Unpacking
print(f"a = {a}, b = {b}, c = {c}")

# Extended unpacking
nums = (1, 2, 3, 4, 5)
x, *y, z = nums
print("x =", x, "y =", y, "z =", z)
print()

# --------------------------------------------------------
print("="*60)
print("9. Nested Tuples")
print("="*60)

nested = ((1, 2), (3, 4))
print("nested[0][1] ->", nested[0][1])
for row in nested:
    print(row)
print()

# --------------------------------------------------------
print("="*60)
print("10. Built-in Functions with Tuples")
print("="*60)

nums = (4, 2, 9, 1)
print("len(nums) ->", len(nums))
print("sum(nums) ->", sum(nums))
print("max(nums) ->", max(nums))
print("min(nums) ->", min(nums))
print("sorted(nums) ->", sorted(nums))  # Returns list
print()

# --------------------------------------------------------
print("="*60)
print("11. Common Misconceptions Recap")
print("="*60)

print("1) Tuples are immutable, but can contain mutable objects.")
print("2) Single-element tuple needs a comma: (value,).")
print("3) No append/remove/sort — use lists if mutability is needed.")
print("4) Tuples can be concatenated or repeated, creating new tuples.")
