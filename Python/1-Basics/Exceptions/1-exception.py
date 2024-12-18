#syntax 
try:
    code 
    code 
except:
    code 
    code 
else:
    code 
    code 
finally:
    code 
    code 


def name(name = "A", Year_born = "B"):
    try:
        A = input("Name: ").strip()
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