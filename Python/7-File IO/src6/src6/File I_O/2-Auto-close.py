names = input("What is your names: ")

with open("list.txt", "a") as file:
    file.write(f"{names}\n")