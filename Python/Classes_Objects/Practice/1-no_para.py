#No parameter

def main():
    name = "zwivhuya"
    last = "Mukwevho"
    full = name + " " + last
    return print(full)

main()

def add():
    x = 2
    y = 4
    sum = x + y
    return print(sum)
add()

def main():
    name = input(str("what is your name: "))
    last = input(str("What is ur surname: "))
    full = name + " " + last
    return print(full)
main()

def add():
    try:
        x = int(input("X: "))
        y = int(input("Y: "))
        sum = x + y
    except ValueError:
        print("X-value/Y-value is not an integer")
    else:
        return print(sum)
add()