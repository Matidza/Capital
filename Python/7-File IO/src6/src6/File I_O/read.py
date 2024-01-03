with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line.rstrip())