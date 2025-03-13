# Creating a class  
class Student:
    def __init__(self,name,grade,cgpa): # method
        self.name=name                # attribute
        self.grade=grade              # attribute
        self.cgpa = cgpa  # attribute
    def student_details(self): # method
        print(f"{self.name} is in {self.grade}ndyr and has {self.cgpa} cgpa")

# Creating variables 
cgpa1 = float(input("Enter cgpa of student 1: "))
cgpa2 = float(input("Enter cgpa of student 2: "))

# Creating objects
student1 = Student("yash",2, cgpa1)
student2 = Student("raviraj",2,cgpa2)

# Printing objects
student1.student_details()
student2.student_details()

# Printing in Key Value pair using __dict__
print(student1.__dict__)
print(student2.__dict__)

# Modify object attribute
student1.cgpa = 9.9        # modify
student1.student_details() # priting after modifying

# del attribute or object
del student2.grade       # will delete grade of student 2
del student1             # will delete student 1 
print(student2.__dict__)    