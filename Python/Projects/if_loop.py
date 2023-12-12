score = float(input("What did you score: "))
if score >= 90  <= 100:
    print("Grade: A\n")
elif score >= 80 <= 89:
    print("Grade: B\n")
elif score >= 70 <= 79:
    print("Grade: C\n")
elif score >= 60 <= 69:
    print("Grade: Fail\n")

name = input("What is your name: ").strip().title()
match name:
    case "Zwivhuya" | "Wanga" | "mukona":
        print(f"{name.strip()} Mukwevho \n")
    case "Thato":
        print("208\n")
    case "Thakane":
        print("207\n")
    case _:
        print("Who? \n")

def even():
    x = int(input("What is x: "))
    if is_even(x):
        print("Even number\n")
    else:
        print("Odd number\n")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

even()