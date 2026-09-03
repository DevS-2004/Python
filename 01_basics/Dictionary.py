# ==========================================================
# PYTHON DICTIONARY COMPLETE CHEATSHEET WITH EXAMPLES
# ==========================================================

# ---- 1. Creating Dictionaries ----

# Empty dictionary
dct = {}
print("Empty dictionary:", dct)

# Dictionary with initial key-value pairs
dct = {"name": "Devendra", "age": 25, "drink": "chai"}
print("Initial dictionary:", dct)

# Using dict() constructor
dct2 = dict(city="Mumbai", country="India")
print("Using dict():", dct2)

# Dictionary with mixed key types
dct3 = {1: "one", "two": 2, (3, 4): "tuple key"}
print("Mixed key types:", dct3)

# ---- 2. Accessing Values ----
print("\n--- Accessing values ---")
print("dct['name'] ->", dct["name"])  # Direct access
# print(dct["invalid"])  # ❌ KeyError if key doesn't exist

# Using get() to avoid KeyError
print("dct.get('drink') ->", dct.get("drink"))
print("dct.get('invalid', 'default value') ->", dct.get("invalid", "default value"))

# ---- 3. Adding / Updating Items ----
print("\n--- Adding / Updating ---")
dct["age"] = 26  # Update existing key
dct["language"] = "Python"  # Add new key
print("After updates:", dct)

# update() method - merges another dictionary
dct.update({"country": "India", "hobby": "coding"})
print("After update():", dct)

# ---- 4. Removing Items ----
print("\n--- Removing items ---")
print("pop('hobby') ->", dct.pop("hobby"))  # Removes key & returns value
# print(dct.pop("invalid"))  # ❌ KeyError if missing
print("pop('invalid', 'not found') ->", dct.pop("invalid", "not found"))

print("popitem() ->", dct.popitem())  # Removes & returns last inserted item (tuple)
print("After popitem():", dct)

del dct["drink"]  # Delete by key
print("After del:", dct)

dct.clear()  # Removes all items
print("After clear():", dct)

# ---- 5. Dictionary from List / Tuples ----
print("\n--- From list/tuples ---")
pairs = [("a", 1), ("b", 2)]
d_from_pairs = dict(pairs)
print("From list of tuples:", d_from_pairs)

# ---- 6. Looping through Dictionary ----
print("\n--- Looping ---")
dct = {"name": "Devendra", "drink": "chai", "age": 25}
for key in dct:
    print("Key:", key, "| Value:", dct[key])

for key, value in dct.items():
    print(f"{key} -> {value}")

print("Keys:", list(dct.keys()))
print("Values:", list(dct.values()))
print("Items:", list(dct.items()))

# ---- 7. Dictionary Comprehensions ----
print("\n--- Dictionary Comprehensions ---")
squares = {x: x**2 for x in range(5)}
print("Squares dict:", squares)

# ---- 8. Nested Dictionaries ----
print("\n--- Nested dictionary ---")
nested = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested)
print("nested['person1']['name'] ->", nested["person1"]["name"])

# ---- 9. Misconceptions / Gotchas ----
print("\n--- Misconceptions & Gotchas ---")

# Mutable default value pitfall
shared_list = []
dict_with_list = {"a": shared_list, "b": shared_list}
dict_with_list["a"].append(100)
print("Shared list in dict (both changed):", dict_with_list)

# Keys must be hashable (immutable)
# d = {[1, 2]: "list as key"}  # ❌ TypeError: unhashable type: 'list'
d = {(1, 2): "tuple as key"}  # ✅ Tuples can be keys
print("Tuple as key:", d)

# Dictionary ordering (Python 3.7+ maintains insertion order)
ordered = {"first": 1, "second": 2, "third": 3}
print("Insertion order preserved:", ordered)

# Copying dictionaries
original = {"a": 1, "b": 2}
copy1 = original.copy()
copy2 = dict(original)
copy1["a"] = 100
print("Original unaffected after copy():", original)

# Shallow copy & nested structures
nested_original = {"a": [1, 2], "b": [3, 4]}
shallow_copy = nested_original.copy()
shallow_copy["a"].append(99)
print("Shallow copy affects original:", nested_original)

# Deep copy to avoid mutation issues
import copy
deep_copy = copy.deepcopy(nested_original)
deep_copy["a"].append(1000)
print("After deepcopy, original unaffected:", nested_original)

# ==========================================================
# END OF DICTIONARY CHEATSHEET
# ==========================================================
print("End of dictionary cheatsheet.")
print("="*50)
# ==========================================================