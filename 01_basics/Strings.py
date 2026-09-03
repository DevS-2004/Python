# string_methods_demo.py
# Demonstrates important Python string methods/functions and their tricky parts

print("="*50)
print("1. str() vs print() vs repr()")
print("="*50)

s = "chai"
print("str(s)  ->", str(s))       # returns 'chai' (no quotes in the string itself)
print("repr(s) ->", repr(s))      # returns "'chai'" (quotes part of the content)
print("print(s):", end=" "); print(s)  # displays without quotes
print()

print("In REPL, typing str(s) would show quotes because REPL uses repr()")
print()

# --------------------------------------------------------
print("="*50)
print("2. len(), indexing, slicing")
print("="*50)

s = "Python"
print("len(s)      ->", len(s))
print("s[0]        ->", s[0])      # First character
print("s[-1]       ->", s[-1])     # Last character
print("s[0:4]      ->", s[0:4])    # Slice (up to but not including index 4)
print("s[::-1]     ->", s[::-1])   # Reverse string
print()

# --------------------------------------------------------
print("="*50)
print("3. Case conversion")
print("="*50)

s = "PyThOn"
print("s.lower()   ->", s.lower())
print("s.upper()   ->", s.upper())
print("s.title()   ->", s.title())
print("s.capitalize() ->", s.capitalize())
print("s.swapcase()   ->", s.swapcase())
print()

# --------------------------------------------------------
print("="*50)
print("4. strip(), lstrip(), rstrip()")
print("="*50)

s = "   chai   "
print(f"Original: >{s}<")
print("s.strip()  ->", s.strip())    # removes spaces both ends
print("s.lstrip() ->", s.lstrip())   # removes spaces left side
print("s.rstrip() ->", s.rstrip())   # removes spaces right side
print()

# --------------------------------------------------------
print("="*50)
print("5. replace(), split(), join()")
print("="*50)

s = "I like tea"
print("s.replace('tea', 'coffee') ->", s.replace("tea", "coffee"))
print("'one,two,three'.split(',')  ->", "one,two,three".split(","))
print("'-'.join(['2025','08','11']) ->", "-".join(["2025","08","11"]))
print()

# --------------------------------------------------------
print("="*50)
print("6. find(), index(), rfind()")
print("="*50)

s = "banana"
print("s.find('na')  ->", s.find("na"))   # first occurrence
print("s.rfind('na') ->", s.rfind("na"))  # last occurrence
# print(s.index('xy')) # would raise ValueError if not found
print()

# --------------------------------------------------------
print("="*50)
print("7. count(), startswith(), endswith()")
print("="*50)

s = "banana"
print("s.count('na')      ->", s.count("na"))
print("s.startswith('ba') ->", s.startswith("ba"))
print("s.endswith('na')   ->", s.endswith("na"))
print()

# --------------------------------------------------------
print("="*50)
print("8. isalpha(), isdigit(), isalnum(), isspace()")
print("="*50)

print("'abc'.isalpha() ->", "abc".isalpha())
print("'123'.isdigit() ->", "123".isdigit())
print("'abc123'.isalnum() ->", "abc123".isalnum())
print("'   '.isspace() ->", "   ".isspace())
print()

# --------------------------------------------------------
print("="*50)
print("9. encode(), decode()")
print("="*50)

s = "chai"
encoded = s.encode("utf-8")
print("s.encode('utf-8') ->", encoded)
print("encoded.decode('utf-8') ->", encoded.decode("utf-8"))
print()

# --------------------------------------------------------
print("="*50)
print("10. format(), f-strings, % formatting")
print("="*50)

name = "Dev"
age = 25
print("Hello, {}!".format(name))
print("Hello, {1}. You are {0}.".format(age, name))
print(f"Hello, {name}. You are {age}.")   # f-string
print("Hello, %s. You are %d." % (name, age))
print()

# --------------------------------------------------------
print("="*50)
print("11. Escapes, raw strings")
print("="*50)

print("Line1\nLine2")      # newline in output
print(r"Line1\nLine2")     # raw string - no escape processing
print()

# --------------------------------------------------------
print("="*50)
print("12. Common confusions recap")
print("="*50)

print("repr('chai') ->", repr("chai"), " (includes quotes)")
print("str('chai')  ->", str("chai"), " (just the text)")
print("print('chai') shows:", end=" "); print("chai")
print("'abc'.find('z') ->", "abc".find("z"), " (returns -1, NOT error)")
print("'abc'.index('z') -> would ERROR if run")

path = r"c:\user\OneDrive\Devendra\\"
print(path)

