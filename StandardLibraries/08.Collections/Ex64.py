from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

st1 = {'name': 'Kate', 'age': 20, 'specialization': 'mathematics'}
st2 = {'name': 'Mike', 'age': 21, 'specialization': 'physics'}
st3 = {'name': 'Bob', 'age': 21, 'specialization': 'information technology'}

students = [Student(**st1), Student(**st2), Student(**st3)]

for student in students:
    print(student)