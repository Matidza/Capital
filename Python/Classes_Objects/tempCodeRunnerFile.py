class info:
    def __init__(self,name, surname, age, skills= 'b', address= 'a'):
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = skills
        self.address = address
        try:
            b = ["Python", "Bash", "Java Script", "Django"]
            a = {
                "street: ": "Rixile strt", "House: ": "No: 2002", 
                "Surbub: ": "Tshikota Location", "Town: ": "Makhado",
                "Province: ": "Limpopo", "Country: ": "South Africa",
                "Zip code: ": "0920",
            }
            return f"Info: {name} + ' ' + {surname}\n {age} \n{skills} \n {address}"
        except:
            print("Thats a mouth full")
person = info("zwivhuya", "Mukwevho", "26", )
print(person.name)
print(person.surname)
print(person.age)
print(person.skills)
print(person.address)