#
#
# Purpose: Another class generated to for inheritance principle
# Outputs: Generates identification for faculty and students via
#          inheritance principle
#

class Person:
    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        
        # self.id generates ID number and definition may be equal to
        # a method but, remember to add 'self.' to call the method
        self.id = self.generate_id()
        self.courses = []

    def generate_id(self):
        id_hash = 0
        for i in self.name:
            # ord() function returns the unicode identifier
            id_hash += ord(i)
        for i in self.surname:
            id_hash += ord(i)
        id_hash = id_hash % int(1e10)
        return id_hash
        
    def __str__(self):
        return 'Name: '+self.surname + ', '+self.name+ '\nCourses: '\
            +str(self.courses)

class Student(Person):
    # Student class will be based on the Person class by putting the
    # Person as an argument
    def __init__(self,name,surname,age,gender):
        # super() function looks for operations in Person class
        super().__init__(name,surname,age,gender)

# Testing the inheritance principle for students
student1 = Student('Sam','Ellis',30,'Male')
print(student1)
print(student1.id)
print(student1.__dict__)

class Faculty(Person):
    # Faculty class may be generated using features from the Person class
    def __init__(self,name,surname,age,gender,position):
        super().__init__(name,surname,age,gender)
        self.position = position
        self.courses = []
