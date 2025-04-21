import random
from sympy import isprime, mod_inverse

# Function to find a prime number
def get_prime(bitsize=8):
    while True:
        prime = random.getrandbits(bitsize)
        if prime > 2 and isprime(prime):  # Ensure prime is large enough
            return prime

# Function to find a primitive root modulo p
def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors(p - 1)):
            return g
    return None

# Function to get the factors of a number
def factors(n):
    result = set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            result.add(d)
            n //= d
        d += 1
    if n > 1:
        result.add(n)
    return result

# Key generation
def generate_keys(bitsize=8):
    p = get_prime(bitsize)  # Select a large prime p
    g = find_primitive_root(p)  # Select a primitive root g
    x = random.randint(2, p - 2)  # Private key
    y = pow(g, x, p)  # Public key (y = g^x mod p)
    return (p, g, y), x  # Public key and private key

# ElGamal encryption
def encrypt(public_key, message):
    p, g, y = public_key
    k = random.randint(2, p - 2)  # Random integer for encryption
    c1 = pow(g, k, p)  # c1 = g^k mod p
    c2 = (message * pow(y, k, p)) % p  # c2 = m * y^k mod p
    return c1, c2

# ElGamal decryption
def decrypt(private_key, ciphertext):
    p, g, y = public_key
    x = private_key  # Private key
    c1, c2 = ciphertext
    s = pow(c1, x, p)  # s = c1^x mod p
    s_inv = mod_inverse(s, p)  # Inverse of s mod p
    message = (c2 * s_inv) % p  # m = c2 * s^-1 mod p
    return message

# Example usage with user input
if __name__ == "__main__":
    # Generate keys
    public_key, private_key = generate_keys(bitsize=8)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Take user input for the message to encrypt
    message = int(input("Enter the message (as an integer): "))
    print("\nOriginal Message:", message)

    # Encrypt the message
    ciphertext = encrypt(public_key, message)
    print("Ciphertext:", ciphertext)

    # Decrypt the message
    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted Message:", decrypted_message)
