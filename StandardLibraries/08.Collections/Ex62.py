from collections import namedtuple

Student = namedtuple("Student", ['name', 'age', 'specialization'])

mike = Student('Mike', 21, 'physics')
kate = Student('Kate', 20, 'mathematics')
bob = Student('Bob', 21, 'information technology')

students = [mike, kate, bob]

for student in students:
    print(f"{student.name:5} : {student.age} : {student.specialization}") 