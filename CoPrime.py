def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return euclidean_gcd(a, b) == 1

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Checking if they are co-prime
if are_coprime(a, b):
    print(f"{a} and {b} are co-prime (GCD = 1).")
else:
    print(f"{a} and {b} are NOT co-prime (GCD ≠ 1).")
