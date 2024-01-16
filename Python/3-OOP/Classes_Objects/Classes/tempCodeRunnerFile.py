class Student:
    def __init__(self, name,surname,code,degree):
        self.name = name
        self.surname = surname
        self.code = code
        self.degree = degree
        self.skills = []

    def __str__(self):
        return f"\nNames: {self.name} {self.surname} \nStudent No: {self.degree} \nDegree: {self.code}\nSkills: {self.skills}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise  TypeError("Names/Surnames must be in letters")
        else:
            self.__name = name
    
    #Surname
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self,surname):
        if not isinstance(surname, str): raise TypeError("Names/Surnames must be in letters") 
        else:
            self.__surname = surname

    #Code
    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self,code):
        try:
            self.__code = code
        except ValueError:
            print("Code must be integeres.")
            
    #Degree
    @property
    def degree(self):
        return self.__degree
    
    @degree.setter
    def degree(self,degree):
        try:
            self.__degree = degree
        except TypeError:
            print("Degree must be in letters!")

def add_skills(self, skills):
    self.skills.append(skills)

def main():
    student_card = get_card()
    print(student_card)

def get_card():
    name = input("What is your name: ")
    surname = input("What is your surname: ")
    degree = input("What degree are you enrolled in")
    code = int(input("Student number: "))
    return Student(name, surname, degree, code)

# Append Skills """



info = Student()
info.add_skills("Python")
info.add_skills("C")
info.add_skills("Java Script")
info.add_skills("Django")
print("\nObject Method to Modify class Default Values")

if __name__ == "__main__":
    main()        
