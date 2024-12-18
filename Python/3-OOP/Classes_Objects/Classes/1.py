class P:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x
    
    def set_x(self):
        self.__x = x

p1 = P(2)
print(p1.get_x())



class P:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1001)
print(p1.get_x())

