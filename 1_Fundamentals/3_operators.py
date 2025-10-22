# A comprehensive program to demonstrate all operators in Python

# --- 1. Arithmetic Operators ---
print("--- 1. Arithmetic Operators ---")
a = 10
b = 4
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponent (a ** b): {a ** b}\n")


# --- 2. Assignment Operators ---
print("--- 2. Assignment Operators ---")
c = 15
print(f"Initial c: {c}")
c += 5  # c = c + 5
print(f"After c += 5: {c}")
c *= 2  # c = c * 2
print(f"After c *= 2: {c}\n")


# --- 3. Comparison Operators ---
print("--- 3. Comparison Operators ---")
print(f"Is a ({a}) == c ({c})? {a == c}")
print(f"Is a ({a}) != b ({b})? {a != b}")
print(f"Is a ({a}) > b ({b})? {a > b}\n")


# --- 4. Logical Operators ---
print("--- 4. Logical Operators ---")
has_key = True
is_locked = False
print(f"Has key: {has_key}, Is locked: {is_locked}")
# Check if you can open the door
if has_key and not is_locked:
    print("Result: You can open the door.")
# Check if you need a key OR the door is already unlocked
if has_key or not is_locked:
    print("Result: You can get through.\n")


# --- 5. Identity Operators ---
print("--- 5. Identity Operators ---")
list_x = [1, 2, 3]
list_y = [1, 2, 3]
list_z = list_x
print(f"list_x = {list_x}, list_y = {list_y}, list_z = list_x")
print(f"list_x == list_y (checks value): {list_x == list_y}")
print(f"list_x is list_y (checks memory location): {list_x is list_y}")
print(f"list_x is list_z (checks memory location): {list_x is list_z}\n")


# --- 6. Membership Operators ---
print("--- 6. Membership Operators ---")
my_message = "hello world"
my_numbers = [1, 5, 8, 10]
print(f"Message: '{my_message}', Numbers: {my_numbers}")
print(f"Is 'world' in my_message? {'world' in my_message}")
print(f"Is 7 not in my_numbers? {7 not in my_numbers}\n")


# --- 7. Bitwise Operators ---
print("--- 7. Bitwise Operators ---")
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print(f"x = {x} (1010), y = {y} (0100)")
print(f"AND (x & y): {x & y} (0000)")
print(f"OR (x | y): {x | y} (1110 -> 14)")
print(f"XOR (x ^ y): {x ^ y} (1110 -> 14)")
print(f"NOT (~x): {~x} (inverts bits)")
print(f"Left Shift (x << 2): {x << 2} (101000 -> 40)")
print(f"Right Shift (x >> 2): {x >> 2} (0010 -> 2)")