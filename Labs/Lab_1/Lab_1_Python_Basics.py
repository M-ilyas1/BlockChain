# Importing a built-in module
import math  # The math module provides mathematical functions

# Using Python as a calculator
result = 5 * 2 + math.sqrt(16)  # Performing arithmetic operations
print("The result of the calculation is:", result)  # Output the result

# Demonstrating variable types
integer_var = 10  # Integer
float_var = 20.5   # Float
string_var = "Hello, Python!"  # String
boolean_var = True  # Boolean

print("\nVariable Types:")
print("Integer:", type(integer_var))  # Should show <class 'int'>
print("Float:", type(float_var))      # Should show <class 'float'>
print("String:", type(string_var))    # Should show <class 'str'>
print("Boolean:", type(boolean_var))  # Should show <class 'bool'>

# Converting data types
string_number = str(integer_var)  # Convert integer to string
print("\nConverted Integer to String:", string_number)

# Taking user input
user_name = input("Enter your name: ")  # User input, stored as a string
print("Hello, " + user_name + "!")  # Greet the user

# Demonstrating string functions
sample_string = "hello world"
print("\nString Functions:")
print("Length of string:", len(sample_string))  # Length of the string
print("Does it end with 'world'? ", sample_string.endswith("world"))  # Check if ends with 'world'
print("Count of 'l':", sample_string.count('l'))  # Count occurrences of 'l'
print("Capitalized string:", sample_string.capitalize())  # Capitalize first letter
print("Index of 'world':", sample_string.find('world'))  # Find index of 'world'
print("Replaced string:", sample_string.replace('world', 'Python'))  # Replace 'world' with 'Python'

# Working with lists
my_list = [1, 2, 3, "apple", "banana"]
print("\nList Operations:")
print("Original list:", my_list)
my_list.append("cherry")  # Append an item
print("After appending 'cherry':", my_list)
my_list.insert(2, "orange")  # Insert an item at index 2
print("After inserting 'orange' at index 2:", my_list)
my_list.pop(1)  # Remove item at index 1
print("After popping item at index 1:", my_list)
my_list.remove("banana")  # Remove first occurrence of 'banana'
print("After removing 'banana':", my_list)
my_list.sort()  # Sort the list
print("Sorted list:", my_list)

# Working with tuples
my_tuple = (5, 10, 15, 20)
print("\nTuple Operations:")
print("Original tuple:", my_tuple)
print("Count of 10 in tuple:", my_tuple.count(10))  # Count occurrences of 10
print("Index of 15 in tuple:", my_tuple.index(15))  # Find index of 15
