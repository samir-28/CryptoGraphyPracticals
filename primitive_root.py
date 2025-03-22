def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    required_set = {num for num in range(1, p) if euclidean_gcd(num, p) == 1}
    actual_set = {pow(g, powers, p) for powers in range(1, p)}
    return required_set == actual_set

p = int(input("Enter a prime number: "))
for g in range(2, p):
    if is_primitive_root(g, p):
        print(f"{g} is a primitive root of {p}")
