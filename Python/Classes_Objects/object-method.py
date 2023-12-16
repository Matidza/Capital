# Object Method
class person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def person_info(self):
        return f"{self.name} {self.surname} is {self.age} years old"
    
info = person("Zwivhuya", "Nukwevho", "26")
print(info.person_info())

# Object Default Methods
class info:
    def __init__(self, name= "zwivhuya", last= "Mukwevho", age= "26"):
        self.name = name
        self.last = last
        self.age = age
    def person(self):
        return  f"{self.name} {self.last} is {self.age} years old"
    
p = info()
print(p.person())
p1 = info("wanga", "Mukwevho" ,"23")
print(p1.person())