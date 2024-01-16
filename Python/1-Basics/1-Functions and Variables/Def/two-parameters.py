#SYNTAX
# def main(para1, para2):
#    code 
#    code 
#    code 
# print(main(arg1, arg2))

# Examples
# No:1
def full_name(Name, Surname):
    full = print(Name + " " + Surname)
    return full
full_name("\nZwivhuya", "Mukwevho")

# No:2
def sum(num1, num2):
    add = num1 + num2
    return add
print(f"\n{sum(2, 7)}")

# No:3
def weight(mass, gravity):
    weight = str(int(mass * gravity)) +" N"
    return print(weight)
weight(60, 9.8)

# UPGRADE THE ABOVE DEF FUNCTION
# Passing Arguments with Keya and Values
print(f"\nUpdate")

# No:1
def full_nam(name, surname):
    full = print(name + " " + surname)
    return full
full_nam(name= input("Name? "), surname= input("Surname? "))

# No:2
def summ(num1, num2):
    add = print(num1 + num2)
    return add
summ(num1= 2, num2= 1)

# No: 3
def weight(mass, gravity):
    weight = str(int(mass) * int(gravity)) +" N"
    return print(weight)
weight(mass= 55, gravity= 9.82)