import pickle


class Person:
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = 185
        

person = Person('Mark', 24, 185)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)