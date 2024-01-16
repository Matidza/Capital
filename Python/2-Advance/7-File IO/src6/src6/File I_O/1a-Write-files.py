names = input("what is your name: ")
file = open("text.txt", "w") # Write on a file
file.write(names)
file.close()