def additive_inverse(a, mod):
    """
    Computes the additive inverse of a under modulo 'mod'.
    The additive inverse of 'a' is (-a) % mod.
    """
    return (-a) % mod

def multiplicative_inverse(a, mod):
    """
    Computes the multiplicative inverse of 'a' under modulo 'mod' using the Extended Euclidean Algorithm.
    The multiplicative inverse exists only if gcd(a, mod) = 1.
    """
    original_mod = mod
    x0, x1 = 0, 1
    while a > 1:
        q = a // mod  # Quotient
        a, mod = mod, a % mod  # Apply Euclidean algorithm
        x0, x1 = x1 - q * x0, x0  # Update x

    if a == 1:  # If gcd(a, mod) == 1, return the inverse
        return x1 % original_mod
    else:
        return None  # No inverse exists if gcd(a, mod) ≠ 1

# Taking user input
a = int(input("Enter a number: "))
mod = int(input("Enter modulo: "))

# Compute inverses
add_inv = additive_inverse(a, mod)
mul_inv = multiplicative_inverse(a, mod)

# Print results
print(f"Additive Inverse of {a} mod {mod} = {add_inv}")
if mul_inv is not None:
    print(f"Multiplicative Inverse of {a} mod {mod} = {mul_inv}")
else:
    print(f"Multiplicative Inverse does not exist for {a} mod {mod}")
