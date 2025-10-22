# A program demonstrating all control flow statements
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop a specific number of times using range()
for i in range(5): # will loop from 0 to 4
    print(f"Loop number {i}")

    
# --- Game Setup ---
inventory = []
current_room = "hall"
game_running = True
key_found = False

print("--- Welcome to the Mini Adventure! ---")
print("Your goal is to find the key and unlock the treasure door.")
print("Commands: 'look', 'get key', 'go north', 'go south', 'unlock door', 'quit'")

# --- Main Game Loop (while) ---
# The game runs as long as this condition is true
while game_running:
    print("\n" + "="*25)
    # The 'for' loop iterates over the items in the inventory list
    print("Your inventory:")
    if not inventory:
        print("- empty -")
    else:
        for item in inventory:
            print(f"- {item}")
    
    print(f"You are in the {current_room}.")
    
    command = input("What do you do? > ").lower()

    # --- Conditional Statements (if/elif/else) ---
    if current_room == "hall":
        if command == "go north":
            current_room = "library"
            print("You enter a dusty library.")
        elif command == "go south":
            print("You see a large, locked treasure door.")
            current_room = "treasure_room"
        elif command == "look":
            print("You are in a grand hall. There are doors to the north and south.")
        else:
            print("Invalid command in the hall.")
            # 'continue' skips the rest of this iteration and starts the next one
            continue

    elif current_room == "library":
        if command == "look":
            if not key_found:
                print("You see a messy desk with a shiny 'key' on it.")
            else:
                print("You see a messy desk. The key is gone.")
        elif command == "get key":
            if not key_found:
                print("You picked up the key!")
                inventory.append("key")
                key_found = True
            else:
                print("You already have the key.")
        elif command == "go south":
            current_room = "hall"
            print("You return to the hall.")
        else:
            print("Invalid command in the library.")
            continue
            
    elif current_room == "treasure_room":
        if command == "unlock door":
            if "key" in inventory:
                print("🎉 Congratulations! You unlocked the door and found the treasure!")
                # 'break' terminates the main 'while' loop immediately
                break
            else:
                print("The door is locked. You need a key.")
        elif command == "go north":
            current_room = "hall"
            print("You return to the hall.")
        else:
            print("Invalid command at the treasure door.")
            continue
    
    # Check for a quit command at any point
    if command == "quit":
        print("You decide to leave the adventure for another day.")
        break

print("\n--- GAME OVER ---")