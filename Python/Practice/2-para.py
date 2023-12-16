def info(name, last):
    full = name + " " + last
    return print(full)
info("Zwivhuya", "Mukwevho")

def add(num1, num2):
    sum = num1 + num2
    return print(sum)
add(12, 35)

# Inputs + Exceptions

def info(Name, Last_name):
    try:
        Name = str(input("Name: "))
        Last_name = str(input("Surname: "))
        full = Name + " " + Last_name
        return print(f"\n{full}")
    except NameError:
        print("Name/Surname is not a string.")
info(1, 1)


def add(num1,  num2= "a"):
    try:
        a = num2= int(input("num2: "))
        sum = num1 + num2
        return print(sum)
    except ValueError:
        print("Values enterewd not integers!")
add(num1= int(input("num1: ")))
