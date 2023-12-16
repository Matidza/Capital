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