students = input("Students in the class: ")
file = open("student-list.txt", "a")
file.write(f"{students}\n")
file.close()