# 🐍 Python Study Notes

> Personal reference notes covering core Python concepts, internals, and gotchas.

---

## 📑 Table of Contents

1. [Bytecode & Module Reloading](#1-bytecode--module-reloading)
2. [Assignment Operators](#2-assignment-operators)
3. [Identity vs Equality](#3-identity-vs-equality)
4. [Garbage Collection](#4-garbage-collection)
5. [Data Types Overview](#5-data-types-overview)
6. [Operations on Data Types](#6-operations-on-data-types)
7. [Type Conversion](#7-type-conversion)
8. [Mutable vs Immutable](#8-mutable-vs-immutable)
9. [Operator Precedence](#9-operator-precedence)
10. [Dictionaries — Deep Dive](#10-dictionaries--deep-dive)
11. [How Python Works Internally](#11-how-python-works-internally)

---

## 1. Bytecode & Module Reloading

### Bytecode Files (`.pyc`)

- When you **run a file directly**, the bytecode is hidden/internal.
- When a file **imports another file**, Python creates a `.pyc` bytecode cache:

```
__pycache__/imported_file_name.cpython-3xx.pyc
```

### Reloading a Module at Runtime

```python
from importlib import reload
reload(module_name)   # Forces Python to re-read and re-execute the module
```

> **Why?** Python caches imported modules. `reload()` is needed when the source file changes during a running session.

---

## 2. Assignment Operators

### `a = a + 1`
- Standard **assignment statement**.
- Takes current value of `a`, adds 1, assigns result back.
- **Always creates a NEW object** (for immutable types like `int`).

### `a += 1`
- **Compound assignment** (shorthand).
- For **immutable types** (int, str, tuple) → same result as `a = a + 1`.
- For **mutable types** (list) → modifies the object **in-place**.

### Key Difference with Lists

```python
a = [1, 2]
b = a

# Using +=  → modifies in-place, b is also affected
a += [3]
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]  ← b changed too!

# Using = + → creates a new list, b is NOT affected
a = a + [3]
print(a)  # [1, 2, 3]
print(b)  # [1, 2]     ← b unchanged
```

> ⚡ **Rule:** `+=` modifies the list in-place. `= list + [item]` creates a new list.

---

## 3. Identity vs Equality

| Operator | Checks | Example |
|----------|--------|---------|
| `==` | **Value** equality | `[1,2] == [1,2]` → `True` |
| `is` | **Reference** (same object in memory) | `[1,2] is [1,2]` → `False` |

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)   # True  — same values
print(a is b)   # False — different objects
print(a is c)   # True  — c points to the same object as a
```

> **Note:** For small integers (-5 to 256) and interned strings, Python may reuse the same object, so `is` can return `True` unexpectedly. Don't rely on `is` for value comparisons.

---

## 4. Garbage Collection

- Python uses **reference counting** + a **cyclic garbage collector**.
- When a variable is reassigned, the old object's reference count drops.
- When count reaches **0**, memory is freed.

```python
a = 10   # Object 10 is created, ref count = 1
a = 20   # Object 10's ref count drops to 0 → eligible for GC
```

> ⚠️ **Exception:** For **numbers** and **strings**, Python uses **interning/caching**, so GC may not happen immediately — small objects are kept around for reuse.

---

## 5. Data Types Overview

| Category | Types |
|----------|-------|
| **Numeric** | `int`, `float`, `complex`, `Decimal`, `Fraction` |
| **Sequence** | `str`, `list`, `tuple` |
| **Mapping** | `dict` |
| **Set** | `set`, `frozenset` |
| **Boolean** | `bool` (`True` / `False`) |
| **None** | `NoneType` |
| **Binary** | `bytes`, `bytearray`, `memoryview` |

### Boolean behaves like int

```python
True + 5     # → 6
False + 10   # → 10
True * 3     # → 3
bool(0)      # → False
bool("")     # → False
bool([])     # → False
bool(1)      # → True
```

---

## 6. Operations on Data Types

### Arithmetic Operators

| Type | Supported Operators | Notes |
|------|---------------------|-------|
| `int`, `float`, `complex` | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Mixing int+float → float |
| `str` | `+`, `*` | `+` = concat, `*` = repeat |
| `list`, `tuple` | `+`, `*` | `+` = concat, `*` by int only |
| `bool` | Same as `int` | `True=1`, `False=0` |
| `None` | ❌ None | Raises `TypeError` |

### Common TypeError Traps

```python
"10" + 5          # ❌ TypeError — no implicit conversion
"abc" - "a"       # ❌ TypeError — subtraction not supported on strings
[1,2] + (3,4)     # ❌ TypeError — list + tuple not allowed
"abc" * 2.0       # ❌ TypeError — must multiply by int, not float
None + 1          # ❌ TypeError — None is not a number
complex(1,2) > 3  # ❌ TypeError — complex has no ordering
```

### Division Rules

```python
10 / 2    # → 5.0   (always float!)
10 // 2   # → 5     (floor division — integer result)
-7 // 2   # → -4    (floors towards -infinity, not towards 0)
10 % 3    # → 1     (modulo / remainder)
2 ** 10   # → 1024  (power)
```

---

## 7. Type Conversion

### Explicit Conversion (Type Casting)

```python
int("42")        # → 42
int(3.9)         # → 3   (truncates, doesn't round)
float("3.14")    # → 3.14
str(100)         # → "100"
bool(0)          # → False
bool("hello")    # → True
list((1,2,3))    # → [1, 2, 3]
tuple([1,2,3])   # → (1, 2, 3)
```

> Python **never** does implicit conversion between strings and numbers. Always convert explicitly.

### Debug with `type()`

```python
x = 3.14
print(type(x))         # <class 'float'>
print(type(x).__name__) # 'float'
```

---

## 8. Mutable vs Immutable

| Immutable (cannot change in-place) | Mutable (can change in-place) |
|------------------------------------|-------------------------------|
| `int`, `float`, `complex` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `bool` | `bytearray` |
| `frozenset` | |

### Why it matters

```python
# Immutable — new object is created
a = "hello"
b = a
a += " world"
print(b)  # "hello"  — b is unchanged

# Mutable — same object is modified
a = [1, 2]
b = a
a.append(3)
print(b)  # [1, 2, 3]  — b is changed!
```

> 💡 **Rule:** To safely copy a mutable object, use `.copy()` or `copy.deepcopy()`.

---

## 9. Operator Precedence

Highest → Lowest:

| Priority | Operator | Description |
|----------|----------|-------------|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary operators |
| 4 | `*`, `/`, `//`, `%` | Multiplication / Division |
| 5 | `+`, `-` | Addition / Subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | Comparisons | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |

```python
# Example
result = 2 + 3 * 4 ** 2   # → 2 + 3 * 16 → 2 + 48 → 50
```

---

## 10. Dictionaries — Deep Dive

### What is a Dictionary?

A **mutable**, ordered (Python 3.7+) collection of **key-value pairs**.

```python
my_dict = {key1: value1, key2: value2}
```

- **Keys** → must be **immutable/hashable** (str, int, tuple)
- **Values** → can be **anything**

### Common Gotchas

| Gotcha | Explanation |
|--------|-------------|
| Duplicate keys | Last value wins |
| Mutable keys | ❌ `TypeError: unhashable type` |
| Default iteration | Gives **keys only**, not values |
| Shallow copy | Nested objects still share references |

### Examples

**Duplicate keys — last wins:**
```python
d = {"a": 1, "b": 2, "a": 3}
print(d)  # {"a": 3, "b": 2}
```

**Mutable value — reference behavior:**
```python
list1 = [1, 2]
d = {"numbers": list1}
list1.append(3)
print(d)  # {"numbers": [1, 2, 3]}  ← changed!
```

**Invalid key (mutable type):**
```python
d = {[1, 2]: "test"}    # ❌ TypeError: unhashable type: 'list'
d = {(1, 2): "test"}    # ✅ Tuples are hashable
```

**Nested dictionary:**
```python
student = {
    "name": "Ishu",
    "marks": {"math": 90, "science": 95}
}
print(student["marks"]["science"])  # 95
```

**Iteration:**
```python
d = {"a": 10, "b": 20}

for key in d:               # iterates over keys
    print(key)

for key, val in d.items():  # iterates over key-value pairs
    print(key, val)
```

**Shallow vs Deep Copy:**
```python
import copy

original = {"numbers": [1, 2]}
shallow  = original.copy()
deep     = copy.deepcopy(original)

original["numbers"].append(3)

print(shallow)   # {"numbers": [1, 2, 3]}  ← affected!
print(deep)      # {"numbers": [1, 2]}     ← safe!
```

### Useful Dictionary Methods

| Method | Description |
|--------|-------------|
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| `.items()` | Returns `(key, value)` pairs |
| `.get(key, default)` | Returns value or `default` if key missing |
| `.update(other_dict)` | Merges another dict into this one |
| `.pop(key)` | Removes key and returns its value |
| `.setdefault(key, val)` | Sets key if not present, returns its value |
| `.clear()` | Removes all items |

```python
employee = {
    "name": "Arsh",
    "id": 101,
    "skills": ["Python", "SQL"],
    "salary": {"basic": 50000, "bonus": 10000}
}

print(employee.get("age", "Not Found"))   # "Not Found"
print(employee["skills"][0])              # "Python"
print(employee["salary"]["bonus"])        # 10000
```

---

## 11. How Python Works Internally

### Execution Pipeline

```
┌─────────────────────────┐
│   Python Source Code    │  (.py file)
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Tokenization (Lexer)   │  Breaks code into tokens
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│   Parsing (AST)         │  Builds Abstract Syntax Tree
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Bytecode Compilation   │  Generates .pyc in __pycache__
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Python Virtual Machine │  Executes bytecode instructions
│         (PVM)           │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ Execution + Memory Mgmt │  GC, reference counting
│   + Garbage Collector   │
└─────────────────────────┘
```

### Why is Python Slower Than Compiled Languages?

| Reason | Explanation |
|--------|-------------|
| **Bytecode, not machine code** | Runs on PVM instead of directly on CPU |
| **Interpreted** | No ahead-of-time compilation to native binary |
| **Dynamic typing** | Types are checked at runtime, not compile time |
| **Runtime overhead** | Every operation involves extra Python-level checks |

> 💡 **Trade-off:** Python sacrifices raw speed for **readability**, **developer productivity**, and **flexibility**.

---

*Last updated: September 2026*
