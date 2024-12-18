# No parameters and return
def gen():
    name = input("Name? ").strip().title()
    surname = input("Surname? ").strip().title()
    Full_name = name + " " + surname
    print(f"{Full_name}\n")
gen()

def gen():
    name = input("Name? ")
    surname = input("Surname? ")
    Full_name = print(f"\n{name + " " + surname}")
    return (Full_name)
gen()

def sum():
    num1 = int(input("What is your number: "))
    num2 = int(input("What is you number: "))
    add = print(f"\n{num1 + num2}")
    return add
sum()

#Different method of return
def sum():
    num1 = int(input("What is your number: "))
    num2 = int(input("What is you number: "))
    add = num1 + num2
    return add
print(sum())

list = []
for i in range(1,6):
    i = list.append("meow")

print(list)