# inheritance_demo.py
# Demonstrating Inheritance in Python

# Base class (Parent)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# Single Inheritance: Student inherits Person
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  # Calling parent constructor
        self.roll_no = roll_no

    def show_student(self):
        return f"{self.show_info()}, Roll No: {self.roll_no}"


# Multilevel Inheritance: GraduateStudent → Student → Person
class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, degree):
        super().__init__(name, age, roll_no)
        self.degree = degree

    def show_graduate(self):
        return f"{self.show_student()}, Degree: {self.degree}"


# Multiple Inheritance
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def show_sport(self):
        return f"Sport: {self.sport}"


class StudentAthlete(Student, Athlete):
    def __init__(self, name, age, roll_no, sport):
        Student.__init__(self, name, age, roll_no)
        Athlete.__init__(self, sport)

    def show_student_athlete(self):
        return f"{self.show_student()}, {self.show_sport()}"


# Testing the inheritance
if __name__ == "__main__":
    s1 = Student("Ishu", 20, 101)
    print(s1.show_student())

    g1 = GraduateStudent("Arsh", 22, 102, "M.Tech")
    print(g1.show_graduate())

    sa1 = StudentAthlete("Jasraj", 21, 103, "Cricket")
    print(sa1.show_student_athlete())
