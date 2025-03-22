import random

def diffie_hellman(p, g):
    # User A selects a secret key
    a = random.randint(1, p-1)
    A = pow(g, a, p)

    # User B selects a secret key
    b = random.randint(1, p-1)
    B = pow(g, b, p)

    # Computing shared secret keys
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    return a, b, A, B, key_A, key_B

# Taking inputs
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root of p (g): "))

a, b, A, B, key_A, key_B = diffie_hellman(p, g)

# Displaying results
print(f"User A's secret key: {a}")
print(f"User B's secret key: {b}")
print(f"User A sends: {A}")
print(f"User B sends: {B}")
print(f"Shared secret key computed by A: {key_A}")
print(f"Shared secret key computed by B: {key_B}")
print(f"Keys match: {key_A == key_B}")
