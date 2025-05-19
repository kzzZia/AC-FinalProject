import random
from math import gcd

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_prime_number():
    while True:
        prime_candidate = random.randint(2**8, 2**9)
        if is_prime(prime_candidate):
            return prime_candidate

def generate_keypair(p, q):
    n = p * q
    totient = (p - 1) * (q - 1)

    e = random.randrange(1, totient)
    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)

    d = pow(e, -1, totient)
    return (e, n), (d, n)

def encrypt(pk, plaintext):
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]

def decrypt(pk, ciphertext):
    key, n = pk
    return ''.join(chr(pow(char, key, n)) for char in ciphertext)

def demo():
    p = generate_prime_number()
    q = generate_prime_number()
    public, private = generate_keypair(p, q)
    message = 'Hello Bob! How are you?'
    cipher = encrypt(public, message)
    plain = decrypt(private, cipher)
    return public, private, message, cipher, plain
