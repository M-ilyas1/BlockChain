# Using Python as a calculator
result = 8 / 4 + 3 
print("Calculator result:", result)

# Variables and Data Types
integer_var = 42
float_var = 3.14
string_var = "Python Programming"
boolean_var = False
none_var = None

print("\nData Types:")
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("NoneType:", none_var)

# Type Conversion
str_var = str(integer_var)
print("\nInteger to String:", str_var)
int_var = int(float_var)
print("Float to Integer:", int_var)
float_var2 = float(integer_var)
print("Integer to Float:", float_var2)

# Taking User Input
user_input = input("Enter a number: ")
print("You entered:", user_input)

# Strings and String Functions
example_string = "Hello, World!"
print("\nString Functions:")
print("Length of string:", len(example_string))
print("String ends with 'World!':", example_string.endswith("World!"))
print("Count of 'o':", example_string.count('o'))
print("Capitalized string:", example_string.capitalize())
print("Replaced string:", example_string.replace('World', 'BlockChain'))

# Lists
my_list = [10, 20, "Hello", True]
print("\nList Operations:")
print("Original list:", my_list)
my_list.append(30)
print("After appending 30:", my_list)
my_list.pop(1)
print("After popping item at index 1:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4)
print("\nTuple Operations:")
print("Original tuple:", my_tuple)
print("Index of 3 in tuple:", my_tuple.index(3))

# Dictionaries
my_dict = {
    "country": "Pakistan",
    "city": "Gilgit",
    "currency_notes": [10, 20, 50, 100]
}
print("\nDictionary Operations:")
print("Country:", my_dict["country"])
print("Currency notes:", my_dict["currency_notes"])
my_dict.update({"city": "Islamabad"})
print("Updated dictionary:", my_dict)

# Sets
my_set = {1, 2, 3, 4}
print("\nSet Operations:")
print("Original set:", my_set)
my_set.add(5)
print("After adding 5:", my_set)
my_set.remove(2)
print("After removing 2:", my_set)
my_set.clear()
print("Set after clearing:", my_set)

# Set operations
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print("Union of sets:", my_set1 | my_set2)
print("Intersection of sets:", my_set1 & my_set2)
