# Variables are containers for storing values.
a = 26
b = "GBIT"
c = 7.99

# Python identifies data types automatically.
print(type(a))
print(type(b))
print(type(c))

# Type Function and Typecasting
print(type(a))

# Typecasting:
str_a = str(a)
int_b = int("26")
float_c = float(32)

# Input Function
user_input = input("Enter your name: ")
print(user_input)

# Strings
single_quote_str = 'Gilgit'
double_quote_str = "Gilgit"
triple_quote_str = '''Gilgit'''

# Lists: Mutable containers
my_list = [2, 4, 7, "Gilgit"]
print(my_list[0])
print(my_list[3])

# List Methods:
my_list = [1, 8, 7, 2, 21, 15]
my_list.sort()
my_list.reverse()
my_list.append(11)
my_list.insert(3, 12)
my_list.pop(2)
my_list.remove(21)


# Dictionaries: Key-value pairs
my_dict = {
    "country": "Pakistan",
    "Province": "GB",
    "City": "Gilgit",
    "Currency Note": [10, 20, 50, 100]
}
print(my_dict["country"]) 
print(my_dict["Currency Note"])


# Sets: Collections of unique elements
my_set = {1, 8, 2, 3}
print(len(my_set))
my_set.remove(8) 
print(my_set)
my_set.add(11)
print(my_set)
my_set.clear()
print(my_set)

# Conditional Expressions
age = int(input("Enter your age: "))
if age >= 26:
    print("Yes")
else:
    print("No")

# Elif Clause
score = 75
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs Improvement")

# While Loop:
i = 0
while i < 5:
    print("BlockChain")
    i += 1

# For Loop:
for item in [1, 3, 5]:
    print(item)


# For Loop with Else:
for item in [1, 3, 5]:
    print(item)
else:
    print("Done")


