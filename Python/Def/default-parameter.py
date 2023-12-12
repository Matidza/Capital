def full_nam(name, surname= "Zwivhuya"):
    full = print(name + " " + surname)
    return full
full_nam("zwivhuya")
full_nam("when", "ok")

# No:2
def summ(num1= int(input("What is num1:")), num2= int(input("What is num2: "))):
    add = print(num1 + num2)
    return add
summ()

# No: 3
def weight(mass, gravity= 9.82):
    weight = str(int(mass) * int(gravity)) +" N"
    return print(weight)
weight(55 )