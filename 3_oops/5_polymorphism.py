# Python's behavior: the second function overwrites the first.
def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

# This would cause an error because the first 'add' function no longer exists.
# print(add(2, 3)) 
# TypeError: add() missing 1 required positional argument: 'c'

print(add(2, 3, 5)) # This works fine.


# Parent class
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def fly(self):
        print("Most birds can fly, but some cannot.")

# Child class 1
class Sparrow(Bird):
    # Overriding the parent's fly() method
    def fly(self):
        print("Sparrows can fly.")

# Child class 2
class Ostrich(Bird):
    # Overriding the parent's fly() method
    def fly(self):
        print("Ostriches cannot fly.")

# Create objects of the classes
sparrow = Sparrow()
ostrich = Ostrich()

# A list containing different objects
birds_in_zoo = [sparrow, ostrich]

# The same method call, .fly(), behaves differently for each object
for bird in birds_in_zoo:
    bird.intro()
    bird.fly()
    print("-" * 15)