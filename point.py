# Point class
class Point :



    def __init__(self,x,y):
        self.x = x
        self.y = y


    def equal(self,other_point) :
        return self.x == other_point.x and self.y == other_point.y

    def isInfinity(self) :
        
        return self.x == -1 and self.y == -1
        
    def __str__(self):
        
        return str(self.x) + "," + str(self.y)

        












