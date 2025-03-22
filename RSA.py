import random

def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b 
    return a

def multiplicative_inverse(a, mod):
    g, x, _ = extended_euclidean(a, mod)
    if g == 1:
        return x % mod
    return None

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def rsa_key_generation():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choosing e (should be co-prime with phi_n)
    e = 3
    while euclidean_gcd(e, phi_n) != 1:
        e += 2

    d = multiplicative_inverse(e, phi_n)
    return (e, n), (d, n)

def rsa_encrypt(message, key):
    e, n = key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, key):
    d, n = key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# RSA Key Generation
public_key, private_key = rsa_key_generation()

message = input("Enter a message to encrypt: ")

# Encrypt and Decrypt
encrypted = rsa_encrypt(message, public_key)
decrypted = rsa_decrypt(encrypted, private_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
