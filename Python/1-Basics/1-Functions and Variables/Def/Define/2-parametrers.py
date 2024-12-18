def main(para):
    code goes here
    code goes heer
#call the function
main(arg)

#Example
def main(name, surname):
    last = print(name + " " + surname)
    return last
main("Zwivhuya", "Mukwevho")

def sum(x, y):
    add = x + y
    return print(f"Sum of x and y is: {add}")
sum(12, 4)

def add_ten(num):
    ten = 10
    return print(num + ten)
add_ten(15)

def age(current_year, birth_year):
    calculate = current_year - birth_year
    return print(calculate)
age(2023, 1997)

def weight(mass, gravity):
    weight = float(str(mass * gravity))
    return print(f"{weight:.2f}", "N")
weight(56, 9.82)