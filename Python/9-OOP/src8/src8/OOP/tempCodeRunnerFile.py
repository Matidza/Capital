import random


class Hat():
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff",
                          "Ravenclaw", "Slytherin"]
        
    def sort(self, name):
        print(name, "is in", random.choice(self.house))


hat = Hat()
hat.sort("Harry")