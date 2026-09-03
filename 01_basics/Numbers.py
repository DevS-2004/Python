import math
import random
from decimal import Decimal

# Set Operation
print({1,2,3} & {2,3,4})  # Output: {2, 3} (intersection of two sets)
print({1,2,3} | {2,3,4})  # Output: {1, 2, 3, 4} (union of two sets)
print({1,2,3} - {2,3,4})  # Output: {1} (difference of two sets)
print({1,2,3} ^ {2,3,4})  # Output: {1, 4} (symmetric difference of two sets)   

# Type of empty paraentheses
print(type(()))  # Output: <class 'tuple'> (empty parentheses represent an empty tuple)
print(type([]))  # Output: <class 'list'> (empty square brackets represent an empty list)
print(type({}))  # Output: <class 'dict'> (empty curly braces represent an empty dictionary)    
print(type(set()))  # Output: <class 'set'> (empty set is created using set())
print(type(1))  # Output: <class 'int'> (1 is an integer)
print(type(1.0))  # Output: <class 'float'> (1.0 is a float)
print(type(1j))  # Output: <class 'complex'> (1j is a complex number with imaginary part 1)
print(type("hello"))  # Output: <class 'str'> (string "hello")
print(type(None))  # Output: <class 'NoneType'> (None is a special constant representing the absence of a value)

# Decimal numbers in Python
d = Decimal('2.23')  # d is a Decimal object representing 2.23
print(d)  # Output: 2.23 (prints the Decimal object)
print(d + 1)  # Output: 3.23 (adds 1 to the Decimal object)
print(d * 2)  # Output: 4.46 (multiplies the Decimal object by 2)
Decimal('2.23') + Decimal('1.77')  # Output: Decimal('4.00') (adds two Decimal objects)
print(0.1+0.2)  # Output: 0.30000000000000004 (due to floating-point precision issues)
print(0.1+0.1+0.1-0.3) 

# Random numbers in Python
random.random()  # Output: A random float between 0.0 and 1.0
random.randint(1, 10)  # Output: A random integer between 1 and 10 (inclusive)
random.choice([1, 2, 3, 4, 5])  # Output: A random element from the list [1, 2, 3, 4, 5]
random.random(3.3)  # Output: A random float between 0.0 and 3.3
random.shuffle([1, 2, 3, 4, 5])  # Output: Shuffles the list in place, e.g., [3, 1, 5, 2, 4]    


math.pi  # Output: 3.141592653589793 (value of pi)
math.floor(2.23)  # Output: 2 (rounds down to the nearest integer)
math.ceil(2.23)  # Output: 3 (rounds up to the nearest integer)
math.sqrt(4)  # Output: 2.0 (square root of 4)
math.pow(2, 3)  # Output: 8.0 (2 raised to the power of 3)
math.factorial(5)  # Output: 120 (factorial of 5)
math.gcd(12, 15)  # Output: 3 (greatest common divisor of 12 and 15)
math.pi + 1  # Output: 4.141592653589793 (pi plus 1)  
math.trunc(2.23)  # Output: 2 (truncates the decimal part, leaving only the integer) 

# Complex numbers in Python
c = 2 + 3j  # c is a complex number with real part 2 and imaginary part 3
# print(c)  # Output: (2+3j) (prints the complex number)
print(c*2 ) # Output: (4+6j) (multiplies the complex number by 2)


# Number representations in Python
print(0b11111111)  # Output: 255 (binary representation of
print(hex(255))  # Output: 'ff' (hexadecimal representation of 255)
print(bin(255))  # Output: '0b11111111' (binary representation of 255)
print(oct(255))  # Output: '0o377' (octal representation of 255)

x = int("64",8)  # Converts the octal string "64" to an integer
print(x)  # Output: 52 (octal 64 is decimal 52)
y = int("8",16)  # Converts the hexadecimal string "8" to an integer
print(y)  # Output: 8 (hexadecimal 8 is decimal 8)
z = int("10",2)  # Converts the binary string "10" to an integer
print(z)  # Output: 2 (binary 10 is decimal 2)

# Arithmetic Shift Operators in Python
a = 1;
print(a << 2)  # Output: 4 (left shift, equivalent to multiplying by 2^2)
print(a >> 2)  # Output: 0 (right shift, equivalent to dividing by 2^2, truncating the decimal part)    


# x = 2;
# y = 3;
# print(x + y)  # Output: 5
# print(x * y)  # Output: 6
# print(x ** y)  # Output: 8 (2 raised to the power of 3)
# print(x / y)  # Output: 0.6666666666666666667 (2 divided by 3)
# print(x // y)  # Output: 0 (2 divided by 3, floor division)
# print(x % y)  # Output: 2 (remainder of 2 divided by 3)
# print(x - y)  # Output: -1 (2 minus 3)

# # Python always givr precedence to highest precedence operator
# print(int(2.23))  # Output: 2 (converts float to int)
# print(2**100)  # Output: 1267650600228229401496703205376 (2 raised to the power of 100)

print(repr("hello")) # Output: 'hello' (string representation of "hello")
print("hello")  # Output: hello (prints the string directly)    
print(str("hello")) # Output: hello (converts to string, same as the original string)
print(repr(2.23))  # Output: '2.23' (string representation of the float)
print(str(2.23))  # Output: 2.23 # (converts to string, same as the original float)
print(repr(2))  # Output: '2' (string representation of the integer)
print(str(2))  # Output: 2 (converts to string, same as the original integer)
print(str([1, 2, 3]))  # Output: [1, 2, 3] (converts list to string)

# true == 1  # Output: True (in Python, True is equivalent to 1)
# false == 0  # Output: True (in Python, False is equivalent to 0)
# print(true)  # Output: True (prints the boolean value True)
# print(false)  # Output: False (prints the boolean value False)  
# true is 1  # Output: False (not only checking value, but also identity; True is not the same object as 1)
