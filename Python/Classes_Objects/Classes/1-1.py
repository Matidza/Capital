# Creayting a class
class person:
    pass
print(person)

# Creating an object
p = person()
print(p)

# **Class constructor**
class info:
    def __init__(self,name):
        self.name = name

p =info("Zwivhuya")
print(f"\n1- Class constructor")
print(p.name)
print(p)

# **Class constructor**- More parameters
class info:
    def __init__(self,name, surname, age, degree):
        self.name = name
        self.surname = surname
        self.age = age
        self.degree = degree

inf = info("Zwivhuya", "Mukwevho", 12, "BCom")
print("\n2- Class constructor- More parameters")
print({inf.name})
print(inf.surname)
print(inf.age)
print(inf.degree)

# Object method
class students:
    def __init__(self,lt= "what"):
        self.lt = lt
        self.lst = []
    
    def print(self):
        return f"{self.lt}"

    def add(self,lst):
        self.lst.append(lst)

 
p = students()
print(p.print())
p.add(45)
p.add("what")
print(p.lst)

# Object Method to Modify class Default Values
class Student:
    def __init__(self, name = input("Name: "), 
                 surname= input("surname: "), code= 43243029,
                 degree= input("course: ")):
         
        self.degree = degree
        self.skills = []

        if not isinstance(name,str):
            raise  TypeError("Names/Surnames must be in letters")
        else:
            self.name = name
        if not isinstance(surname, str): raise TypeError("Names/Surnames must be in letters") 
        else:
            self.surname = surname
        if not isinstance(code, int):
            raise ValueError("Code must be integeres.")
        else:
            self.code = code
    def student_info(self):
        return f"\nNames: {self.name} {self.surname} \nStudent No: {self.code} \nDegree: {self.degree}\nSkills: {self.skills}"
    
    def add_skills(self, skills):
        self.skills.append(skills)

info = Student()
info.add_skills("Python")
info.add_skills("C")
info.add_skills("Java Script")
info.add_skills("Django")
print("Object Method to Modify class Default Values")
print(info.student_info())
        
