# No 1:
try:
    x = int(input("What is x: "))
    y = int(input("What is y: "))
    if x < y or x >y:
        print("x is != y")
    else:
        print("x is == y")
except ValueError:
    print("X/Y must be an integer/number!")

# No 1a:
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("F")


# No 2:
def what():
    try:
        x = int(input("What is your number: "))
        if x < 0:
            x = 0
            print("Negative changed to zero")
        elif x == 0:
            print("Zero")
        elif x > 0:
            print("X is positive")
    except ValueError:
        print("Value must be an integer!")
what()

# No 3:
class name:
    def __init__(self, name= "Zwivhuya", age="a"):
        self.name = name
        self.age = age
        try:
            a = int(input("Age: "))
        except ValueError:
            print("Age must be an integer!")
    def vote(self, value):
        if value <= 17:
            self.age
            print("Don't qualify to vote")
        else:
            self.age
            print("Regiter to vote!")
        return f"{self.name} {self.age}"
                       
p = name()
print(p.vote)

# No 4: 
def main():
    x = int(input("What is x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
main()

name = input("Name: ").title().strip()
match name:
    case "Zwivhuya":
        print(f"{name} mukwevho")
    case "Mukona":
        print(f"{name} mukwevho")
    case "Wanga":
        print(f"{name} mukwevho")
    case "Todani":
        print(f"{name} mukwevho")
    case _:
        print("Who? ")
