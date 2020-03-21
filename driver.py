from point import Point,EllipticCurve
import random







def main():


    RECEIVER_PRIVATE_KEY = 100
    PRIME_NUMBER = 23
    SENDER_RANDOM = random.choice(range(1,PRIME_NUMBER))

    ec = EllipticCurve(1,6,PRIME_NUMBER)

    plain_message = random.choice(ec.points)
    print("Plain message is : " + str(plain_message))

    
    # Encryption
    BASE_POINT = random.choice(ec.points)
    PUBLIC_KEY = ec.multiplication(BASE_POINT,RECEIVER_PRIVATE_KEY)
    
    first_cipher = ec.multiplication(BASE_POINT,SENDER_RANDOM)
    second_cipher = ec.addition(plain_message,ec.multiplication(PUBLIC_KEY,SENDER_RANDOM))

    print("first cipher is : " + str(first_cipher))
    print("second cipher is : " + str(second_cipher))


    # Decryption    
    first_block = ec.multiplication(first_cipher,RECEIVER_PRIVATE_KEY)
    first_block_inv = Point(first_block.x, (-first_block.y)%PRIME_NUMBER)

    retrieved_plaintext = ec.addition(second_cipher,first_block_inv)
    print("retrieved plaintext is : " + str(retrieved_plaintext))


main()