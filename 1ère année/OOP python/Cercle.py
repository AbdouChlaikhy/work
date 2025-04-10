import math
class Cercle:
    def __init__(self,R,x,y):
        self.__R=R
        self.__x=x
        self.__y=y
        
    def getR(self):
        return(self.__R)
    def getC(self):
        return(self.__C)
    def __str__(self) :
        return("centre"+self.__x.__str__()+","+self.__y.__str__()+"rayon="+str(self.__R))
    def __distance__(self):
        return math.sqrt((self.__x)**2+(self.__y)**2)
C1=Cercle(3,2,4)
print(Cercle.__distance__())