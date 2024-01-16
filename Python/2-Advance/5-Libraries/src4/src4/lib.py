import random

#choice()
coin = random.choice(["heads", "Tails"])
print(coin)

print("", sep="")

#randint(a,b)
number = random.randint(1, 20)
print(number)

print("", sep="")

#shuffle(x)
list = [12,"hgjhj", 23, 7657, 8753, "when"]
random.shuffle(list)
for lists in list:
    print(lists, sep="")

print("", sep="")

