#
#
# Purpose: Using the inheritance principle of object oriented programming
# Outputs: Generates identification for faculty and students 
#

class Student:
    # Always initialize class with __init__
    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

        # New courses variable that cannot be overwritten since it is unknown
        # what courses students are taking
        self.courses = []

    # write an enrollment method that takes in a course and adds to
    # the students courses
    def enroll(self,coursename):
#      return self.courses.append(course_name)
       if isinstance(coursename, list):
           self.courses.extend(coursename)
       else:
           self.courses.append(coursename)

    def __str__(self):
       return 'Name: ' + self.surname + ', ' + self.name + '\ncourses: ' + str(self.courses)

class Faculty:
    def __init__(self,name,surname,age,gender,position):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.position = postition

    def assign_course(self, course_name):
        self.courses.append(course_name)

    def __str__(self):
        return 'Name: ' + self.surname + ', ' + self.name + '\ncourses: ' + str(self.courses)
        
# Testing the enrollment function appending course within class Student
student1 = Student('Sam','Ellis',30,'Male')
student1.enroll('Math 101')
student1.enroll(['Phys 101','Chem 101'])
print(student1.courses)
