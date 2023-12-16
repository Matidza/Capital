def info(name, surname):
    full = name + " " + surname
    return print(full)
info(name="zwvhuya", surname= "Mukwevho")

def add(num1, num2):
    sum = num1 + num2
    return print(sum)
add(num1= 12, num2= 2)

def info(name, surname):
    try:
        a = str(input("Name: "))
        b = str(input("Surname: "))
        if isinstance(a,str):
        else:
            print("Name/Surname entered not a string!")
        
        if isinstance(b, str):
            
        else:
            print("Name/Surname entered not a string!")

        full = str(a + " " + b)
    except ValueError:
        print("Name/Surname entered not a string!")
    else:
        return print(full)

info(name= "a", surname="b")

def handsom(Name = "A"):
    while True:
        A = input("Name: ")
        Maybe = float(input("Handsom: "))
        if Maybe >= 7:
            return print( f"{A}\nHandsom")
        else:
            return print(f"{A}\nTry to improve")
handsom()


