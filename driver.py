from point import Point
from ellipticcurve import EllipticCurve
from elGamal import elGamal
import random
import sys






def main():


    PRIVATE_KEY = 100
    prime_number = 4093
    SENDER_RANDOM = random.choice(range(1,prime_number))
    CURVE_A = 1
    CURVE_B = 6
    ENCODING_RANDOM_K = 5

    elGamalClass = elGamal(
        CURVE_A,
        CURVE_B,
        prime_number,
        ENCODING_RANDOM_K,
        SENDER_RANDOM,
        PRIVATE_KEY
    )

    print(elGamalClass)

    plain_message = "Permata hatiku yang indah, aku mencintaimu"
    print("Plain message is : " + str(plain_message))

    cipherpoints = elGamalClass.encrypt(plain_message)
    print("Cipher points are : ")
    for pair in cipherpoints :
        print(str(pair[0]) + " " + str(pair[1]))

    plaintext  = elGamalClass.decrypt(cipherpoints)
    print("Retrieved message is : " + plaintext)
    # Encryption
    #BASE_POINT = random.choice(ec.points)
    #PUBLIC_KEY = ec.multiplication(BASE_POINT,RECEIVER_PRIVATE_KEY)
    

    #print("first cipher is : " + str(first_cipher))
    #print("second cipher is : " + str(second_cipher))


    # Decryption    
    #first_block = ec.multiplication(first_cipher,RECEIVER_PRIVATE_KEY)
    #first_block_inv = Point(first_block.x, (-first_block.y)%prime_number)

    #retrieved_plaintext = ec.addition(second_cipher,first_block_inv)
    #print("retrieved plaintext is : " + str(retrieved_plaintext))

main()