# 'name' is a required parameter.
# 'greeting' and 'is_formal' are optional parameters with default values.
def create_greeting(name, greeting="Hello", is_formal=False):
    """Creates a customizable greeting message."""
    if is_formal:
        message = f"Dear {name},"
    else:
        message = f"{greeting}, {name}!"
    
    return message

# --- Calling the function in different ways ---

# 1. Using only the required positional argument.
#    The function will use the default values for the other parameters.
casual_greeting = create_greeting("Ravi")
print(f"Casual Greeting: {casual_greeting}")

# 2. Using positional arguments to override defaults.
formal_greeting = create_greeting("Dr. Sharma", "Good morning", True)
print(f"Formal Greeting: {formal_greeting}")

# 3. Using keyword arguments to be explicit (order doesn't matter).
#    This is very readable and less prone to errors.
excited_greeting = create_greeting(name="Priya", greeting="Hi")
print(f"Excited Greeting: {excited_greeting}")

# 4. Mixing positional and keyword arguments.
#    Positional arguments must come before keyword arguments.
another_formal_greeting = create_greeting("Mr. Khan", is_formal=True)
print(f"Another Formal Greeting: {another_formal_greeting}")