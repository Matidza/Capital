#Public Attribute
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

x = OurClass(10)
print(x.OurAtt)

class OurClass:

    def __init__(self,a ):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt
    
    @OurAtt.setter
    def OurAttr(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt

x = OurClass(10)
print(x.OurAtt())