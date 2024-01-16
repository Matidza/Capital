with open("student-list.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

""" Or this can be done in this manner"""

with open("student-list.txt", "r") as file:
    for line in file:
        print(f"hello,", line.rstrip())


names = []

with open("student-list.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")