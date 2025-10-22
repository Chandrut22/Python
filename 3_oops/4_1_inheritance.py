# Single Inheritance
# This is the simplest form, where a child class inherits from only one parent class.

class Animal: # Parent class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal): # Child class
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak() # Inherited from Animal
d.bark()  # Its own method


# Multiple Inheritance
# Here, a child class inherits from more than one parent class, combining the features of all parents.


class Bird: # Parent class 1
    def lay_eggs(self):
        print("Laying eggs...")

class Swimmer: # Parent class 2
    def swim(self):
        print("Swimming in water...")

class Penguin(Bird, Swimmer): # Child class
    pass

p = Penguin()
p.lay_eggs() # Inherited from Bird
p.swim()     # Inherited from Swimmer


# Multilevel Inheritance
# In this type, a child class inherits from a parent class, which in turn inherits from a grandparent class. This forms a chain of inheritance.

class Animal: # Grandparent class
    def eat(self):
        print("Eating...")

class Dog(Animal): # Parent class
    def bark(self):
        print("Barking...")

class Puppy(Dog): # Child class
    def weep(self):
        print("Weeping...")

pup = Puppy()
pup.eat()  # Inherited from Animal
pup.bark() # Inherited from Dog
pup.weep() # Its own method


# Hierarchical Inheritance
# This occurs when more than one child class inherits from a single parent class.

class Animal: # Parent class
    def eat(self):
        print("This animal is eating.")

class Dog(Animal): # Child class 1
    pass

class Cat(Animal): # Child class 2
    pass

dog = Dog()
cat = Cat()
dog.eat() # Dog inherits from Animal
cat.eat() # Cat also inherits from Animal


# Hybrid Inheritance
# Hybrid inheritance is a combination of two or more of the above inheritance types. Most often, it's a mix of multiple and multilevel inheritance.

class Animal:
    def live(self):
        print("This animal is alive.")

class Mammal(Animal):
    def feed_milk(self):
        print("Feeds milk.")

class FlyingCreature(Animal):
    def fly(self):
        print("Can fly.")

class Bat(Mammal, FlyingCreature): # Hybrid: Inherits from two classes that share a common parent
    pass

b = Bat()
b.live()      # Inherited from Animal
b.feed_milk() # Inherited from Mammal
b.fly()       # Inherited from FlyingCreature