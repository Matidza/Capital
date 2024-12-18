class P:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = P(1001)
p1.x


# Define a class
class square:
    # Represent a square
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        #get the size of the square
        return (self.__size)
    
    @size.setter
    def size(self, size):
        
        