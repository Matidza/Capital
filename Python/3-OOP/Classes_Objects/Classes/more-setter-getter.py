class robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.potential_physical = lk
        self.potential_psychic = lp
    
    @property
    def condition(self):
        s = self.potential_physical + self.potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be ok!"
        else:
            return "Great!"
        
if __name__ == "__main__":
    x = robot("Zwivhuya", 1979, 0.2, 0.4)
    y = robot("patrick", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)