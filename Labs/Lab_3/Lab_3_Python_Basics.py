# Python Basics Lab 3

# 1. Modules
# A module is a file containing Python code that can be imported and used in other programs.
# Example of built-in modules: os, abc
# Example of external modules: tensorflow, flask

# 2. Using pip to Install Modules
# Pip is a package manager for Python used to install external modules.
# Example command: pip install flask

# 3. Using Python as a Calculator
# You can use Python as a calculator in the REPL (Read-Eval-Print Loop).
# Start the REPL by typing `python` in the terminal.

# 4. Comments
# Single-line comment: Use `#` followed by the comment text.
# Multiline comment: Use triple quotes (`'''` or `"""`).

# 5. Variables and Data Types
# Variables are containers for storing values.
a = 26          # Integer
b = "GBIT"      # String
c = 7.99        # Float

# Python identifies data types automatically.
# Example:
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>

# Rules for defining variable names:
# - Can contain letters, digits, and underscores.
# - Must start with a letter or an underscore.
# - Cannot start with a digit.
# - Cannot be a reserved keyword.

# 6. Operators
# Arithmetic Operators: +, -, *, /, etc.
# Assignment Operators: =, +=, -=, etc.
# Comparison Operators: ==, >, >=, <, !=, etc.
# Logical Operators: and, or, not

# 7. Type Function and Typecasting
# The `type()` function returns the data type of a variable.
print(type(a))  # <class 'int'>

# Typecasting:
# Convert integer to string
str_a = str(a)  # "26"
# Convert string to integer
int_b = int("26")  # 26
# Convert integer to float
float_c = float(32)  # 32.0

# 8. Input Function
# Takes input from the user as a string.
user_input = input("Enter your name: ")  # User input is always a string
print(user_input)

# 9. Strings
# Strings are sequences of characters enclosed in quotes.
single_quote_str = 'Gilgit'
double_quote_str = "Gilgit"
triple_quote_str = '''Gilgit'''

# String Functions:
print(len(single_quote_str))  # Length of the string
print(single_quote_str.endswith("git"))  # Check if it ends with "git"
print(single_quote_str.count("i"))  # Count occurrences of "i"
print(single_quote_str.capitalize())  # Capitalize the first letter
print(single_quote_str.find("git"))  # Find the index of "git"
print(single_quote_str.replace("Gil", "New"))  # Replace "Gil" with "New"

# 10. Lists and Tuples
# Lists: Mutable containers
my_list = [2, 4, 7, "Gilgit"]
print(my_list[0])  # Access the first element
print(my_list[3])  # Access the fourth element
# print(my_list[10])  # IndexError: list index out of range

# List Methods:
my_list = [1, 8, 7, 2, 21, 15]
my_list.sort()  # Sort the list
my_list.reverse()  # Reverse the list
my_list.append(11)  # Add 11 to the end
my_list.insert(3, 12)  # Insert 12 at index 3
my_list.pop(2)  # Remove element at index 2
my_list.remove(21)  # Remove element 21

# Tuples: Immutable containers
my_tuple = (1, 7, 2)
print(my_tuple.count(1))  # Count occurrences of 1
print(my_tuple.index(1))  # Find index of the first occurrence of 1

# 11. Dictionaries and Sets
# Dictionaries: Key-value pairs
my_dict = {
    "country": "Pakistan",
    "Province": "GB",
    "City": "Gilgit",
    "Currency Note": [10, 20, 50, 100]
}
print(my_dict["country"])  # Access value using key
print(my_dict["Currency Note"])  # Access list value

# Dictionary Methods:
print(my_dict.items())  # List of key-value tuples
print(my_dict.keys())  # List of dictionary keys
my_dict.update({"City": "Islamabad"})  # Update dictionary with new key-value pairs
print(my_dict.get("country"))  # Get value of a specified key

# Sets: Collections of unique elements
my_set = {1, 8, 2, 3}
print(len(my_set))  # Length of the set
my_set.remove(8)  # Remove element 8
print(my_set)
my_set.add(11)  # Add element 11
print(my_set)
my_set.clear()  # Clear the set
print(my_set)

# 12. Conditional Expressions
age = int(input("Enter your age: "))
if age >= 26:
    print("Yes")
else:
    print("No")

# 13. Relational Operators
# Examples: ==, >=, <=, <, >

# 14. Logical Operators
# and, or, not

# 15. Elif Clause
# Example:
score = 75
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs Improvement")

# 16. Loops
# While Loop:
i = 0
while i < 5:
    print("GBIT")
    i += 1

# For Loop:
for item in [1, 3, 5]:
    print(item)

# Range Function:
for i in range(0, 7):
    print(i)

# For Loop with Else:
for item in [1, 3, 5]:
    print(item)
else:
    print("Done")

# Break Statement:
for i in range(10):
    if i == 3:
        break
    print(i)

# Continue Statement:
for i in range(4):
    if i == 2:
        continue
    print(i)

# Pass Statement:
for item in [1, 3, 5]:
    pass  # Do nothing

