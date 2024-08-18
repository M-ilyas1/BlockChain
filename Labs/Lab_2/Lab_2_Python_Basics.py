# Importing a built-in module for demonstration
import math  # Provides mathematical functions

# Using Python as a calculator
result = 8 / 4 + math.sqrt(9)  # Basic arithmetic operations and square root
print("Calculator result:", result)

# Variables and Data Types
integer_var = 42  # Integer
float_var = 3.14   # Float
string_var = "Python Programming"  # String
boolean_var = False  # Boolean
none_var = None  # NoneType

print("\nData Types:")
print("Integer type:", type(integer_var))  # <class 'int'>
print("Float type:", type(float_var))      # <class 'float'>
print("String type:", type(string_var))    # <class 'str'>
print("Boolean type:", type(boolean_var))  # <class 'bool'>
print("None type:", type(none_var))        # <class 'NoneType'>

# Type Conversion
str_var = str(integer_var)  # Convert integer to string
print("\nInteger to String:", str_var)
int_var = int(float_var)  # Convert float to integer
print("Float to Integer:", int_var)
float_var2 = float(integer_var)  # Convert integer to float
print("Integer to Float:", float_var2)

# Taking User Input
user_input = input("Enter a number: ")  # User input as string
print("You entered:", user_input)  # Display the input

# Strings and String Functions
example_string = "Hello, World!"
print("\nString Functions:")
print("Length of string:", len(example_string))  # Length of the string
print("String ends with 'World!':", example_string.endswith("World!"))  # Check if ends with 'World!'
print("Count of 'o':", example_string.count('o'))  # Count occurrences of 'o'
print("Capitalized string:", example_string.capitalize())  # Capitalize first letter
print("Index of 'World!':", example_string.find('World!'))  # Find index of 'World!'
print("Replaced string:", example_string.replace('World', 'Python'))  # Replace 'World' with 'Python'

# Lists
my_list = [10, 20, "Hello", True]
print("\nList Operations:")
print("Original list:", my_list)
my_list.append(30)  # Append an item
print("After appending 30:", my_list)
my_list.insert(2, "Insert")  # Insert an item at index 2
print("After inserting 'Insert' at index 2:", my_list)
my_list.pop(1)  # Remove item at index 1
print("After popping item at index 1:", my_list)
my_list.remove("Hello")  # Remove first occurrence of 'Hello'
print("After removing 'Hello':", my_list)
my_list.sort()  # Sort the list
print("Sorted list:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4)
print("\nTuple Operations:")
print("Original tuple:", my_tuple)
print("Count of 2 in tuple:", my_tuple.count(2))  # Count occurrences of 2
print("Index of 3 in tuple:", my_tuple.index(3))  # Find index of 3

# Dictionaries
my_dict = {
    "country": "Pakistan",
    "province": "GB",
    "city": "Gilgit",
    "currency_notes": [10, 20, 50, 100]
}
print("\nDictionary Operations:")
print("Country value:", my_dict["country"])  # Access value using key
print("Currency notes:", my_dict["currency_notes"])  # Access list under key

# Dictionary methods
print("Dictionary items:", my_dict.items())  # List of (key, value) tuples
print("Dictionary keys:", my_dict.keys())  # List of dictionary keys
my_dict.update({"city": "Islamabad"})  # Update dictionary
print("Updated dictionary:", my_dict)
print("Value for 'country':", my_dict.get("country"))  # Get value for 'country'

# Sets
my_set = {1, 2, 3, 4}
print("\nSet Operations:")
print("Original set:", my_set)
my_set.add(5)  # Add item to set
print("After adding 5:", my_set)
my_set.remove(2)  # Remove item from set
print("After removing 2:", my_set)
print("Removed element:", my_set.pop())  # Remove an arbitrary element
print("Set after pop:", my_set)
my_set.clear()  # Clear the set
print("Set after clearing:", my_set)
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print("Union of sets:", my_set1.union(my_set2))  # Union of sets
print("Intersection of sets:", my_set1.intersection(my_set2))  # Intersection of sets
