class info:
    def __init__(self, name, surname, age, skills , address):
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = skills 
        self.address = address 
    
person = info("zwivhuya", "Mukwevho", "26", ["Python", "Java Script"], None )
print(f"Name: {person.name}")
print(f"Surname: {person.surname}")
print(f"age: {person.age}")
print(f"Skills: {person.skills}")
print(f"Address: {person.address}")
