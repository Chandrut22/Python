# Primitive Types
print("-------------- Primitive Types -----------")
my_integer = 100
my_float = 75.5
my_string = "Hello Python"
my_boolean = False

print(f"'{my_integer}' is of type: {type(my_integer)}")
print(f"'{my_float}' is of type: {type(my_float)}")
print(f"'{my_string}' is of type: {type(my_string)}")
print(f"'{my_boolean}' is of type: {type(my_boolean)}")
print("-" * 40)


# Non-Primitive Types
print("----------- Non-Primitive Types -----------")
my_list = [1, "apple", 1]
my_tuple = (2, "banana", 2)
my_dict = {"name": "Charlie", "id": 3}
my_set = {4, "cherry", 4} # The duplicate '4' will be removed

print(f"'{my_list}' is of type: {type(my_list)}")
print(f"'{my_tuple}' is of type: {type(my_tuple)}")
print(f"'{my_dict}' is of type: {type(my_dict)}")
print(f"'{my_set}' is of type: {type(my_set)}")

print("-" * 40)
print("\nPrimitive Type Methods \nFor int, float, and bool, most operations are done with standard operators (+, *, ==, >, etc.) rather than methods. \nThe str type, however, has a rich collection of useful methods for text manipulation.")
print("-------- String Methods --------")


# Convert the entire string to uppercase or lowercase.
my_greeting = "Hello World"
print(my_greeting.upper()) # Output: HELLO WORLD
print(my_greeting.lower()) # Output: hello world


# Remove leading and trailing whitespace from a string.
user_input = "   some data   "
print(user_input.strip()) # Output: 'some data'

# Replace occurrences of a substring with another substring.
sentence = "I like cats."
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence) # Output: I like dogs.

# Split a string into a list based on a delimiter.
csv_data = "John,Doe,35"
data_list = csv_data.split(',')
print(data_list) # Output: ['John', 'Doe', '35']

# Find the index of a substring within a string.
text = "hello python"
print(text.find("python")) # Output: 6
print(text.find("java"))   # Output: -1


print("-" * 40)
print("\nNon-Primitive Type Methods")

print("-------- List Methods --------")
# Adds a single item to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Removes and returns the item at a specific index. If no index is given, it removes the last item.
fruits.pop(0) # Removes 'apple'
print(fruits) # Output: ['banana', 'cherry']

# Sorts the list's items in ascending order.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers) # Output: [1, 2, 3, 4]


print("-------- tuple Methods --------")

# Tuples are immutable, so they have fewer methods. However, you can count occurrences of a value and find the index of a value.
# Returns the number of times a value appears in the tuple.
my_tuple = ('a', 'b', 'c', 'a')
print(my_tuple.count('a')) # Output: 2

# Returns the index of the first occurrence of a value.
print(my_tuple.index('b')) # Output: 1

print("-------- Dictionary Methods --------")

user = {"name": "Charlie", "id": 3}
print(user.keys()) # Output: dict_keys(['name', 'id'])

print(user.values()) # Output: dict_values(['Charlie', 3])

print(user.items()) # Output: dict_items([('name', 'Charlie'), ('id', 3)])

print(user.get("name"))       # Output: Charlie
print(user.get("email"))      # Output: None
print(user.get("email", "not found")) # Output: not found


print("-------- Set Methods --------")

my_set = {1, 2, 3}
my_set.add(4)
my_set.add(2) # This will be ignored
print(my_set) # Output: {1, 2, 3, 4}

my_set.remove(3)
print(my_set) # Output: {1, 2, 4}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b)) # Output: {1, 2, 3, 4, 5}

print(set_a.intersection(set_b)) # Output: {3}