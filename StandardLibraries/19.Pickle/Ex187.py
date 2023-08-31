import pickle


class Person:
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = 185
        

person = Person('Mark', 24, 185)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

with open('person.pkl', 'rb') as f:
    person_loaded = pickle.load(f)

print(person_loaded.name)
print(person_loaded.age)
print(person_loaded.height)

# for attr in person.__dict__.keys():
#     print(getattr(person, attr))