# first type
cats = 3 #start counting from 3 till 1
while cats != 0:
    print("meow")  # for every cat printed, subtract 1 cat till three are printed
    cats = cats - 1 #or cats -= 1

print("\n")
# Second type
cats = 1 # Start counting from 1
while cats <= 3 :
    print("moo")
    cats = cats + 1 #or cats += 1

print("\n")
# third type
cats = 0 # Start counting from 1
while cats < 3 :
    print("heyy")
    cats += 1

print("\n")
#For loop using lists
for num in [1,2,45]:
    print("boo")

print("\n")
#Use a range to demonstrate
for cats in range(3):
    print("!!!!!")

print("\n")

while True:
        n = int(input("what is your Number: "))
        if n <= 0:
            continue
        else:
            break
    
for _ in range(n):
    print("sorry!")       

print("\n")
students = ["Zwivhuya", "Wanga", "Mukona"]
print(students[0])

print("\n")
students = ["Zwivhuya", "Wanga", "Mukona"]
for student in students:
    print(student)

print("\n")
students = ["Zwivhuya", "Wanga", "Mukona"]
for s in range(len(students)):
    print(s + 1, students[s])

#DICTIONARIES
print("\n")
learners = {
    "Zwivhuya": "Mukwvho", 
    "Wanga": "Mukwevho", 
    "Mukona": "Mukwevho",
    "Thato": "208",
    "Thakane": "207",
}
print(learners["Zwivhuya"])
print(learners["Thato"])

print("\n")
learners = {
    "Zwivhuya": "Mukwvho", 
    "Wanga": "Mukwevho", 
    "Mukona": "Mukwevho",
    "Thato": "208",
    "Thakane": "207",
}
for learner in learners:
    print(learner)

# Demonstrates iterating over and index into a dict
print("\n")
learners = {
    "Zwivhuya": "Mukwvho", 
    "Wanga": "Mukwevho", 
    "Mukona": "Mukwevho",
    "Thato": "208",
    "Thakane": "207",
}
for learner in learners:
    print(learner, learners[learner], sep=" ")

# Demonstrates iterating over a list of dict objects
print("\n")
age = int(input("age"))
learners = [
    {f"name": "Zwivhuya", "surname": "Mukwevho", "age": age,}

]
for learner in learners:
    print(learner["name"], learner["surname"], learner["age"])