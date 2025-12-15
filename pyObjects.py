import json

class Humain:
        def __init__(self,name,age,role):
            self.name = name
            self.age = age
            self.role = role

        def display(self):
            return(name, age, role)

personne1 = Humain("Noureddine",18,"Admin")

print(personne1.age)

