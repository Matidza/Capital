class info:
    def __init__(self, name= input("What is your name: "), last= input("Last name: "), age= "20",):
        self.name = name
        self.last = last
        self.age = age
        self.skills = []
    def person(self):
        return  f"\n{self.name} {self.last} is {self.age} years old."
    
    def add_skills(self, skills):
        self.skills.append(skills)


p = info()
print(p.person())
p.add_skills("Python")
p.add_skills("Java Script")
p.add_skills("Django")
print(p.skills)


#Inheritance

class employed(info):
    pass

emp1 = employed("zwichuya", "Mukwevho" , "26")
emp2 = employed("Wanga", "Mukwevho ", "20")
print(emp1.person())
print(emp2.person())