# Point class
class Point :



    def __init__(self,x,y):
        self.x = x
        self.y = y


    def equal(self,other_point) :
        return self.x == other_point.x and self.y == other_point.y

    def isInfinity(self) :
        return self.x == -1 and self.y == -1


# Elliptic curve class
# Equation in the form of y^2 = (x^3 + ax + b) mod p
# Contains information about the curve itself
# However, does not store information about all points in the curve
class EllipticCurve :

    def __init__(self,a,b,p):
        self.a = a
        self.b = b
        self.p = p
    

    # Addition of point
    # return a new point inside the field
    def addition(self,first_point, second_point) :


        # Check for infinity addition
        if first_point.isInfinity() :
            return Point(second_point.x,second_point.y)
        if second_point.isInfinity() :
            return Point(first_point.x,first_point.y)

        if first_point.equal(second_point) :
            # Point self-addition
            return self.self_addition(first_point)
        
        else :
            if first_point.x == second_point.x :
                # Inf
                return Point(-1,-1)
            else :
                gradient = ((first_point.y - second_point.y)/(first_point.x - second_point.x))%self.p
                new_x = (gradient^^2 - (first_point.x + second_point.x))%self.p
                new_y = (gradient(first_point.x - new_x) - first_point.y)%self.p

                return Point(new_x,new_y)

    def self_addition(self,point) :
        if point.y == 0:
            return Point(-1,-1)
        else :
            
            gradient = ((3*point.x + self.a)/(2*point.y))%self.p
            new_x = (gradient^^2 - 2*point.x)%self.p
            new_y = (gradient*(point.x - new_x) - point.y)%self.p
        
            return Point(new_x,new_y)

    # Multiply point n times
    def multiplication(self,point,constant) :
        for _ in range(constant) :
            res_point = self.addition(res_point + point)
        return res_point










