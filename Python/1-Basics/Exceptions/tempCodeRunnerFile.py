def name(name = "A", Year_born = "B"):
    try:
        A = str(input("Name: ")).strip()
        B = int(input("Year born: "))
        Age = 2023 - B
    except TypeError:
        print('Type error occur')
    except ValueError:
        print("Value entered not an integer!")
    except ZeroDivisionError:
        print("Zero division error")    
    else:
        return print(f"You are {A}. And you are {Age} years old or turning {Age} very soon.")
name()