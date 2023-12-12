# Def with Parameters

#declaring the function
#def main(parameter):
#    Code 
#    code 
## Calling the function
#main(argument)

#Examples
# No: 1
def add(num):
    ten = 10
    return num + ten
print(add(80))

def g(name):
    message = name + ', Ok'
    return message
print(g('zwivhuy'))


def greet(name):
    message = print(f"{name + ', welcome to Python'}")
    return message
greet('Thando')

def square(x):
    x = int(input("what is x: "))
    sq = print(x*x)
    return sq
square(4)

def what(n):
    list = []
    for i in range(n):
        i += 1
        b = print(i)
    return b

what(int(input("What is n: ")))


def what(n):
    list = []
    for i in range(n):
        a = {"wanga", "mukona"}
        b = list.append(a)
        i += 1
    b = print(list)
    return b

what(int(input("What is n: "))) 