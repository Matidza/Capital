# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
stud = {"Zwivhuya": "Mukwevho"}

print(stud)
for student in students:
    print(student, students[student], sep=", ")


