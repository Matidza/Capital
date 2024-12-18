class info:
    def __init__(self,name, surname, age, skills , address):
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = skills 
        self.address = address 
    def full(self):
        try:
            b = ["Python", "Bash", "Java Script", "Django"]
            a = {
                "street: ": "Rixile strt", "House: ": "No: 2002", 
                "Surbub: ": "Tshikota Location", "Town: ": "Makhado",
                "Province: ": "Limpopo", "Country: ": "South Africa",
                "Zip code: ": "0920",
            }
            self.skills = b
            self.address = a
            return print(f"Info: {self.name} {self.surname}\n {self.age}\n{self.skills}  {self.address}")
        except:
            print("Thats a mouth full")
person = info("zwivhuya", "Mukwevho", "26", {self.skills}  )
print(person.full())
