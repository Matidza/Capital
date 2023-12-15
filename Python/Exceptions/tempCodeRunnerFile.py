def main():
    try:
        x = int(input("What is x: "))
    except ValueError:
        print("X is not an interger/number")
    else:
        return print(f"X is: {x}") 
    
main()