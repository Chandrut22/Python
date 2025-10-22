# --- Variable Assignments ---
# Python knows this is a string because of the quotes.
student_name = "Priya Sharma"

# Python knows this is an integer because it's a whole number.
student_age = 21

# Python knows this is a float because of the decimal point.
current_gpa = 8.5

# Python knows this is a boolean because its value is True or False.
is_enrolled = True

# Category,Good ✅,Bad ❌,Reason for Error/Bad Practice
# Convention,first_name,FirstName,Not snake_case
# Rule,user_age,2_users,Cannot start with a number
# Rule,_private_var,user-name,Hyphens are not allowed
# Rule,total,for,for is a reserved keyword
# Readability,seconds_per_hour,sph,Not descriptive

# --- Displaying the Variables and Their Types ---
print(f"Student Name: {student_name} (Type: {type(student_name)})")
print(f"Student Age: {student_age} (Type: {type(student_age)})")
print(f"Current GPA: {current_gpa} (Type: {type(current_gpa)})")
print(f"Is Enrolled: {is_enrolled} (Type: {type(is_enrolled)})")


# --- Initial Game Character Stats ---
player_name = "Arjun"
health = 100
score = 0
status_message = "Ready to start!"

print(f"Welcome, {player_name}!")
print(f"Initial Health: {health}, Current Score: {score}")
print(f"Status: {status_message}\n")


# --- Gameplay Event 1: Found a treasure ---
print("You found a treasure chest! It contains 50 points.")
# The 'score' variable is updated using its own previous value.
score = score + 50
status_message = "Feeling lucky!"

print(f"Health: {health}, Current Score: {score}")
print(f"Status: {status_message}\n")


# --- Gameplay Event 2: Encountered a trap ---
damage = 35
print(f"Oh no, a trap! You take {damage} damage.")
# The 'health' variable is updated.
health = health - damage

# The value of a variable is used in a condition.
if health < 70:
    status_message = "Wounded but still fighting!"

print(f"Health: {health}, Current Score: {score}")
print(f"Status: {status_message}\n")


# --- Dynamic Typing in Action ---
# Let's say we want to store more detailed status info.
# The 'status_message' variable is reassigned from a string to a dictionary.
if health <= 65:
    status_message = {
        "condition": "Injured",
        "hp_percentage": (health / 100) * 100
    }
    
print(f"Detailed Status: {status_message} (Type: {type(status_message)})")