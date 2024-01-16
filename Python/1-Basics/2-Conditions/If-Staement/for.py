def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("what is n: "))
        if n > 0:
            break
    return n
def meow(n):
    for i in range(n):
        print("Meow")
main()

words = ["Cats", "Window", "Demonstrate"]

for word in words:
    if word == "Window":
        print(word)
lst = [12, 254, 7854, "Thats ok"]
for word in range(1):
    words.append(lst)
print(words)

name = "Zwivhuya"
for nm in name:
    print(nm, len(nm))

lsty = []
for i in range(1):
    lsty.append([12, 254, 7854, "Thats ok"])
print(lsty)

i = 3
while i != 0:
    i -= 1
    print("meow")

i = 1
while i <= 3:
    i += 1
    print("meow")

name = "Zwivhuya"
for z in name:
    print(z)

students = ["zwivhuya", "Mukona", "Wanga"]
for student in range(len(students)):
    print(student + 1, students[student])

while True:
    n = int(input("what is n: "))
    if n < 0:
        continue
    else:
        break
for _ in range(n):
    print("meoq")

for i in range(3):
    print("meow")


while True:
    try:
        n = int(input("What is n: "))
    except ValueError:
        print("n must be an integer!")   
    for i in range(n):
        print("Meow")
break

