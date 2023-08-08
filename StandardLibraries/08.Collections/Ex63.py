from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = [
    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
    ]

students.sort(key=lambda student: student.age)

print(students)