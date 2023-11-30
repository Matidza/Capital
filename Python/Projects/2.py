#!/usr/bin/python3
#0
print("Zero pro")
def num():
    x = int(input("What is your number: "))
    print(f"{x} is my number")
    print(f"x becomes a floating number: {x:.2f}") 
    print(sep="")
num()

#1
print("Frist pro")
string = ["Zwi", "ok", "rft", "wedr"]
for str in range(len(string)):
    print(str + 1, string[str])
print(sep="")

#2
print("Second pro")
num = "Zwivhuya"
name =  ["Zwivhuya", "Mukona", "Wanga", "Todani", "208"]
first = name[:3]
fir = num[2:]
print(f"This prints the fist 3: {first}, from the list")
print(f"This removes the two letters \'{fir}\', from the string")
print(sep="")

#3
print("third pro")
import random


hey = ["Zwi", "ok", "rft", "wedr"]
string = random.choice(hey)
print(string)


random.shuffle(hey)
for h in hey:
    print(h,sep=" ")


strings = random.randint(1, 20)
if strings >= 10:
    print(f"String is graeter than {strings}.")
else:
    print(f"String is less than {strings}.")
print(sep="")

#4
print("Fourth pro")
import random

number = 1
while number <= 50:
    num = random.randint(1, 50)
    if num <= 25:
        print(f"{num} is less than 25.")
        break
    else:
        print(f"{num} is greater than 25.")
        break
    number += 1
