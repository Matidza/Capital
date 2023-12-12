def bill():
    name = input("What is your name? ")
    ammount = float(input("You owe us. "))
    due_date = str("25/12/2023")
    print(f"Hello {name}")
    print(f"Your outsatnding balance is R{ammount:.2f}", f"That is due on {due_date}")

bill()
                    