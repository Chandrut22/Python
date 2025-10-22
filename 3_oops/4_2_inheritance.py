# 1. Base Class (Top of the hierarchy)
class Person:
    """A base class to represent a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_basic_info(self):
        print(f"Name: {self.name}, Age: {self.age}", end='')

# 2. Child Class (Demonstrates Single Inheritance from Person)
class Student(Person):
    """Represents a student, inheriting from Person."""
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Initialize parent class attributes
        self.student_id = student_id
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}.")

    def display_basic_info(self): # Method Overriding
        super().display_basic_info()
        print(f", Student ID: {self.student_id}")

# 3. Child Class (Demonstrates Hierarchical Inheritance with Student)
class Staff(Person):
    """Represents a staff member, inheriting from Person."""
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_basic_info(self): # Method Overriding
        super().display_basic_info()
        print(f", Employee ID: {self.employee_id}, Dept: {self.department}")

# 4. Grandchild Class (Demonstrates Multilevel Inheritance)
class Professor(Staff):
    """Represents a professor, inheriting from Staff."""
    def __init__(self, name, age, employee_id, department, subject):
        super().__init__(name, age, employee_id, department)
        self.subject = subject
        self.publications = []

    def add_publication(self, publication_title):
        self.publications.append(publication_title)
        print(f"Prof. {self.name} added publication: '{publication_title}'")

    def display_basic_info(self): # Method Overriding
        super().display_basic_info()
        print(f", Subject: {self.subject}")

# --- Main execution block ---
if __name__ == "__main__":
    # Create instances of each class
    student1 = Student("Priya Sharma", 20, "S12345")
    prof1 = Professor("Dr. Rohan Gupta", 45, "E9876", "Computer Science", "Artificial Intelligence")
    staff1 = Staff("Anil Kumar", 35, "E5432", "Admissions")
    
    print("--- University Roster ---")
    
    # Demonstrate unique behaviors and overridden methods
    student1.display_basic_info()
    student1.enroll_in_course("Machine Learning")
    
    print("-" * 25)
    
    staff1.display_basic_info()
    
    print("-" * 25)
    
    prof1.display_basic_info()
    prof1.add_publication("A Study on Neural Networks")
    
    print("\n--- Polymorphism Demonstration ---")
    # All objects can be treated as 'Person' objects
    university_people = [student1, prof1, staff1]
    
    for person in university_people:
        # The correct version of display_basic_info() is called for each object
        person.display_basic_info()