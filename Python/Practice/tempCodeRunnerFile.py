def  info(name= "a", surname= "b"):
    try:
        a = str(input("Name: "))
        b = str(input("Surname"))
        full_info = str(a + " " b)
    except NameError:
        print("Name entered is not a string")
    else:
        return print(full_info)

info() 