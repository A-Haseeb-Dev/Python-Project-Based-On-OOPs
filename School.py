from abc import ABC, abstractmethod

# Abstract Base Class — Abstraction
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod       # Polymorphism (child classes will override this)
    def getDetails(self):
        pass



class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.__grades = grades  # Private field — Encapsulation

    def getDetails(self):       # Polymorphism
        return f"Student: {self.name}, Age: {self.age}, Grades: {self.__grades}"

    def get_grades(self):
        return self.__grades

    def set_grades(self, new_grades):
        self.__grades = new_grades



class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.__salary = salary    # Encapsulation
        self.subject = subject

    def getDetails(self):         # Polymorphism
        return f"Teacher: {self.name}, Subject: {self.subject}, Salary: {self.__salary}"

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary = amount



class Staff(Person):
    def __init__(self, name, age, role, salary):
        super().__init__(name, age)
        self.role = role
        self.__salary = salary    # Encapsulation

    def getDetails(self):         # Polymorphism
        return f"Staff: {self.name}, Role: {self.role}, Salary: {self.__salary}"

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary = amount



students = [
    Student("Ali", 16, {"Math": 85, "Science": 90}),
    Student("Sara", 17, {"Math": 92, "Science": 88})
]

teachers = [
    Teacher("Mr. Khan", 40, 75000, "Math"),
    Teacher("Ms. Ayesha", 35, 80000, "Science")
]

staff = [
    Staff("Ahmad", 30, "Admin", 35000),
    Staff("Bilal", 28, "Cleaner", 20000)
]

print("\n--- SCHOOL MEMBERS LIST ---")
for person in students + teachers + staff:
    print(person.getDetails())
