<div align="center">

# 🐍 Python Learning Journey

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=3776AB&center=true&vCenter=true&random=false&width=435&lines=Learning+Python+from+Scratch;Core+Concepts+%26+OOP;Practice+%2B+Projects" alt="Typing SVG" />

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-DevS--2004-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevS-2004)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> A structured collection of Python concepts, practice exercises, and mini-projects — from fundamentals to advanced topics.

</div>

---

## 📖 About

This repository documents my hands-on Python learning journey. Each folder covers a specific concept with theory, examples, and solved practice problems to reinforce understanding.

---

## 🗂️ Repository Structure

```
Python/
│
├── 📁 01_basics/              # Core Python foundations
│   ├── hello.py               # Hello World & getting started
│   ├── Numbers.py             # Number types & arithmetic operations
│   ├── Strings.py             # String methods & manipulation
│   ├── List.py                # Lists — creation, slicing, methods
│   ├── Tuple.py               # Tuples & immutability
│   ├── Dictionary.py          # Dictionaries — key-value pairs, methods
│   ├── Scopes_Closure.py      # Variable scopes & closures
│   └── basic2.py              # Additional basics
│
├── 📁 Conditionals/           # Decision making in Python
│   ├── questions.md           # Practice questions
│   └── 01–10_solution.py      # 10 solved problems
│
├── 📁 loops/                  # Iteration & looping
│   ├── questions.md           # Practice questions
│   └── 01–10_solution.py      # 10 solved problems
│
├── 📁 Functions/              # Functions, parameters & scope
│   ├── Function.py            # Core function concepts
│   ├── questions.md           # Practice questions
│   └── 01–10_solution.py      # 10 solved problems
│
├── 📁 Decorators/             # Python decorators & higher-order functions
│   ├── decorators.py          # Decorator theory & examples
│   └── 01–03_solution.py      # 3 solved problems
│
├── 📁 Oops/                   # Object-Oriented Programming
│   ├── Oops.py                # Classes, objects & OOP concepts
│   ├── Inheritence.py         # Single & multiple inheritance
│   ├── Polymorphism.py        # Method overriding & duck typing
│   ├── Encapsulation.py       # Access modifiers & data hiding
│   ├── Abstraction.py         # Abstract classes & interfaces
│   └── Accessibility.py       # Attribute accessibility
│
├── 📁 Error_Handling/         # Exception handling & file I/O
│   ├── yt_manager.py          # YouTube manager mini-project
│   └── youtube.txt            # Data file for yt_manager
│
├── 📁 attributes/             # Python attributes & modules
│   ├── calculator.py          # Calculator module
│   └── main.py                # Entry point
│
└── 📄 notes.md                # Personal study notes & key concepts
```

---

## 📚 Topics Covered

| 🏷️ Topic | 📋 Concepts Covered | 🔢 Exercises |
|----------|---------------------|-------------|
| **Basics** | Numbers, Strings, Lists, Tuples, Dicts, Scopes | Core Files |
| **Conditionals** | if / elif / else, nested conditions, match-case | 10 Problems ✅ |
| **Loops** | for, while, break, continue, comprehensions | 10 Problems ✅ |
| **Functions** | args/kwargs, lambda, recursion, closures | 10 Problems ✅ |
| **Decorators** | Higher-order functions, @decorator syntax, chaining | 3 Problems ✅ |
| **OOP** | Classes, Inheritance, Polymorphism, Encapsulation, Abstraction | Concept Files |
| **Error Handling** | try/except/finally, custom exceptions, file I/O | Mini Project ✅ |
| **Attributes** | Module attributes, imports, __name__ | Calculator App ✅ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed → [Download Python](https://www.python.org/downloads/)
- A code editor (VS Code recommended)

### Clone the Repository

```bash
git clone https://github.com/DevS-2004/Python.git
cd Python
```

### Run Any File

```bash
# Example — run the YouTube manager project
python Error_Handling/yt_manager.py

# Example — explore OOP concepts
python Oops/Oops.py

# Example — test decorator concepts
python Decorators/decorators.py
```

---

## 💡 Key Concepts & Quick Notes

<details>
<summary><b>🔢 Data Types</b></summary>

| Type | Example | Mutable |
|------|---------|---------|
| `int` | `42` | ❌ |
| `float` | `3.14` | ❌ |
| `str` | `"hello"` | ❌ |
| `list` | `[1, 2, 3]` | ✅ |
| `tuple` | `(1, 2, 3)` | ❌ |
| `dict` | `{"a": 1}` | ✅ |
| `set` | `{1, 2, 3}` | ✅ |

</details>

<details>
<summary><b>🧬 OOP Pillars</b></summary>

- **Encapsulation** — Bundle data and methods; hide internal details using `_` or `__`
- **Inheritance** — Reuse parent class behaviour in child classes
- **Polymorphism** — Same interface, different behavior (method overriding / duck typing)
- **Abstraction** — Expose only what is necessary using `ABC` and `@abstractmethod`

</details>

<details>
<summary><b>🎯 How Python Works Internally</b></summary>

```
Python Source Code
      ↓
Tokenization (Lexer)
      ↓
Parsing (AST)
      ↓
Bytecode Compilation (.pyc)
      ↓
Python Virtual Machine (PVM)
      ↓
Execution + Memory Management + GC
```

</details>

<details>
<summary><b>⚡ Important Rules to Remember</b></summary>

- `10 / 2` → `5.0` (always float), use `//` for integer division
- `True = 1`, `False = 0` — booleans behave like integers
- `+=` on lists modifies **in-place**; `= list + [item]` creates a **new list**
- `m == n` checks **value**; `m is n` checks **reference**
- Dictionary keys must be **hashable** (immutable types only)

</details>

---

## 🛠️ Mini Projects

| Project | Description | Location |
|---------|-------------|----------|
| 🎬 **YouTube Manager** | CLI app to manage a YouTube video list using file I/O & error handling | [`Error_Handling/yt_manager.py`](Error_Handling/yt_manager.py) |
| 🧮 **Calculator Module** | Modular calculator demonstrating Python module attributes | [`attributes/calculator.py`](attributes/calculator.py) |

---

## 📈 Progress Tracker

- [x] Python Basics (Numbers, Strings, Lists, Tuples, Dicts)
- [x] Conditionals — 10/10 problems solved
- [x] Loops — 10/10 problems solved
- [x] Functions — 10/10 problems solved
- [x] Decorators — 3/3 problems solved
- [x] Object-Oriented Programming (all 4 pillars)
- [x] Error Handling & File I/O
- [ ] Generators & Iterators *(coming soon)*
- [ ] File Handling Deep Dive *(coming soon)*
- [ ] Modules & Packages *(coming soon)*

---

## 📬 Connect with Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-DevS--2004-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevS-2004)

</div>

---

<div align="center">

**⭐ If this repo helped you, consider giving it a star!**

*Happy Coding! 🚀*

</div>
