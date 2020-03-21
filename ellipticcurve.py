from point import Point
import math
# Elliptic curve class
# Equation in the form of y^2 = (x^3 + ax + b) mod p
# Contains information about the curve itself
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
                delta_x = (first_point.x - second_point.x)
                gradient = ((first_point.y - second_point.y)*self.__modulo_invers(delta_x))%self.p
                new_x = (gradient**2 - (first_point.x + second_point.x))%self.p
                new_y = (gradient*(first_point.x - new_x) - first_point.y)%self.p

                return Point(new_x,new_y)

    def self_addition(self,point) :
        if point.y == 0:
            return Point(-1,-1)
        else :

            gradient = ((3*(point.x**2) + self.a)*self.__modulo_invers(2*point.y))%self.p
            new_x = (gradient**2 - 2*point.x)%self.p
            new_y = (gradient*(point.x - new_x) - point.y)%self.p
        
            return Point(new_x,new_y)

    # Multiply point n times
    def multiplication(self,point,constant) :
        if constant == 1:
            return Point(point.x, point.y)
        if constant%2 == 0:
            return self.self_addition(self.multiplication(point,math.floor(constant/2)))
        else :
            temp_point = self.multiplication(self.multiplication(point,math.floor(constant/2)),2)
            return self.addition(temp_point,point)


    # Finding the invers of num mod p
    # There should be an invers, 
    def __modulo_invers(self,num):
        for i in range(1,self.p):
            if (num*i)%self.p == 1 :
                return i
        
        return 0

    # Generate point for base
    # Return as an array of list of y for value x
    def generatePoints(self,x):
        temp_list = []
        remainder = self.y(x)
        for y in range(1,self.p) :
                if y**2%self.p == remainder :
                    temp_list.append(y)

        return temp_list

    def y(self,x):
        return (x**3 + self.a*x + self.b)%self.p
                    