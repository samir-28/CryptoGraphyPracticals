def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = euclidean_algorithm(a, b)
print(f"GCD using Euclidean Algorithm: {gcd}")

gcd, x, y = extended_euclidean_algorithm(a, b)
print(f"GCD using Extended Euclidean Algorithm: {gcd}")
print(f"Coefficients x and y: {x}, {y}")