# No module import needed

# Using Python as a calculator
result = 5 * 2 + 4  # The square root of 16 is 4
print("The result of the calculation is:", result)  # Output the result

# Demonstrating variable types
integer_var = 10
float_var = 20.5
string_var = "Hello, Python!"
boolean_var = True

print("\nVariable Types:")
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

# Converting data types
string_number = str(integer_var)
print("\nConverted Integer to String:", string_number)

# Taking user input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# Demonstrating string functions
sample_string = "hello world"
print("\nString Operations:")
print("Length of string:", len(sample_string))
print("Count of 'l':", sample_string.count('l'))
print("Capitalized string:", sample_string.capitalize())

# Working with lists
my_list = [1, 2, 3, "apple", "banana"]
print("\nList Operations:")
print("Original list:", my_list)
my_list.append("cherry")
print("After appending:", my_list)
my_list.pop(1)
print("After popping item at index 1:", my_list)

# Working with tuples
my_tuple = (5, 10, 15, 20)
print("\nTuple Operations:")
print("Original tuple:", my_tuple)
print("Index of 15 in tuple:", my_tuple.index(15))
