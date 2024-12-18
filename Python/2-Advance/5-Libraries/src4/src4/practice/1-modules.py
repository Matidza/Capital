import random

secret_santer = random.choice(["Mariam", "TK", "Mpumi", "Thanyani",
                               "Wife", "Zwivhuya", "Khodani", "Todani"])

print(secret_santer)


#from
from random import choice
coin = choice(["fio", "Zwi"])
print(coin)

#Randint
import random
number = random.randint(1, 10)
print(number)

import random
cards = ["king", "jack", "Queeen"]
random.shuffle(cards)
for card in cards:
    print(card)