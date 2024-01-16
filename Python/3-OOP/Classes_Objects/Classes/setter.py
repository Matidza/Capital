class p:
    def __init__(self, x):
        self.__x = x

    @property
    #get x
    def x(self):
        return self.__x
    
    @x.setter
    # Set x
    def x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = p(1001)
print(p1.x())

# Thus use this
class p:
    def __init__(self, x):
        self.__x = x

    @property
    #get x
    def x(self):
        return self.__x
    
    @x.setter
    # Set x
    def x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = p(1001)
print(p1.x())
