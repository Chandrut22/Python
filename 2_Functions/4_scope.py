# GLOBAL variable to track the score
score = 0

def display_score():
    """This function READS the global score."""
    print(f"Current score is: {score}")

def increase_score(points):
    """This function MODIFIES the global score."""
    # Use the 'global' keyword to indicate we want to change the global 'score' variable
    global score
    score += points
    print(f"{points} points added!")

# --- Gameplay Simulation ---
print("--- Starting Game ---")
display_score()

# The player finds a treasure
increase_score(50)
display_score()

# The player completes a quest
increase_score(100)
display_score()

print("--- Game Over ---")