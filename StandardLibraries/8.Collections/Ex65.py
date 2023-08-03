from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

# List to store dictionaries
students = []

# Load dictionaries from the text file
with open('StandardLibraries\8.Collections\students.txt', 'r') as file:
    for line in file:
        students.append(eval(line))


print(students)
