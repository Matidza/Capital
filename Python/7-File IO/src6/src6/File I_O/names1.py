names = input("What is your name: ")

with open("name.txt", "a") as file:
    file.write(f"{names}\n")


