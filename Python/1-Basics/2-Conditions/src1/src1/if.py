# Age
age = int(input("age: "))
if age <= 17:
    print("Don't qualify to vote")
else:
    print("You qualify to vote.")

print('\n')

# Marks
marks = int(input("marks: "))
if marks >= 90:
    print("A: Passed")
elif marks >= 80:
    print("B: Passed")
elif marks >= 70:
    print("C: Passed")
else:
    print("F: Failed")

# Match
name = input("What is your name? ")
match name:
    case "Zwivhuya" | "Wanga" | "Mukona":
        print("Mukwevho")
    case "Thakane":
        print("Pabane")
    case "Thato":
        print("208")
    
