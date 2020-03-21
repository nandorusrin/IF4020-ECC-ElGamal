# ElGamal encryption/decrypion class\
from ellipticcurve import EllipticCurve
from point import Point
import random
import math


class elGamal :


    # Parameters for curve and encoding
    # For encoding, see Readme.
    def __init__(self,curve_a,curve_b,prime,random_k,sender_random,private_key,encoding='ascii'):
        self.private_key = private_key
        self.prime_number = prime
        self.sender_random = sender_random
        self.ec = EllipticCurve(curve_a,curve_b,prime)
        self.random_k = random_k
        self.encoding = encoding

        # Generate random point for base
        self.__generateBase()

        # Generate public key
        self.public_key = self.ec.multiplication(self.base_point,private_key)



    def encrypt(self,plaintext) :
        # Encoded plaintext should be list of points.
        # List of points can be made from chunks of plaintext
        ciphertext_points = []
        encoded_points = self.__encode_plaintext(plaintext)
        for point in encoded_points :
            ciphertext_points.append(self.__encrypt_point(point))
        return ciphertext_points

    def decrypt(self,cipherpoints) :
        plaintext_points = []
        for point_pair in cipherpoints :
            plaintext_points.append(self.__decrypt_point_pair(point_pair))
        
        return self.__decode_points(plaintext_points)

    
    def __generateBase(self):
        found = False
        while not found :
            x = random.choice(range(1,self.prime_number))
            y_list = self.ec.generatePoints(x)
            if len(y_list) > 0:
                found = True
                self.base_point = Point(x,random.choice(y_list))

    def __encode_plaintext(self,plaintext):
        byte_array = bytearray(plaintext,self.encoding)
        chunks_list = []
        for byte in byte_array :

            for j in range(self.random_k) :
            # Solve for y
                x = byte*self.random_k + j
                list_of_y = self.ec.generatePoints(x)
                if len(list_of_y) > 0:
                    y = random.choice(list_of_y)
                    chunks_list.append(Point(x,y))
                    break
        
        return chunks_list

    # Return as string
    def __decode_points(self,plaintext_points):
        string = ""
        for point in plaintext_points :
            string += chr(math.floor((point.x)/self.random_k))
        return string




    def __encrypt_point(self,point):
        first_cipher = self.ec.multiplication(self.base_point,self.sender_random)
        second_cipher = self.ec.addition(point,self.ec.multiplication(self.public_key,self.sender_random))

        return [first_cipher,second_cipher]

    def __decrypt_point_pair(self,point_pair) :
        first_block = self.ec.multiplication(point_pair[0],self.private_key)
        first_block_inv = Point(first_block.x, (-first_block.y)%self.prime_number)

        return self.ec.addition(point_pair[1],first_block_inv)


    def __str__(self):
        string = "Parameters :\n"
        string += "Private key : " + str(self.private_key) + "\n"
        string += "Public key : " + str(self.public_key) + "\n"
        string += "Prime used : " + str(self.prime_number) + "\n"
        string += "Base point : " + str(self.base_point) + "\n"
        string += "Sender random number : " + str(self.sender_random) + "\n"
        string += "Random k used for encoding : " + str(self.random_k) + "\n"

        return string
