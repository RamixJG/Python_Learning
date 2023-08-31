class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        

Mark = Person("Mark", 24, 185)

print(Mark.name)
print(Mark.age)
print(Mark.height)