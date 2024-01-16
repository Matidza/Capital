with open("student-list.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

""" This can be done like this"""

with open("student-list.csv") as file:
    print(f"This can be like this: \n")
    for line in file:
        name, last = line.rstrip().split(",")
        print(f"{name}, {last}")