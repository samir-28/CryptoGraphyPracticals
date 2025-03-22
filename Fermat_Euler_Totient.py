def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def phi(n):
    result = 1
    for i in range(2, n):
        if euclidean_gcd(i, n) == 1:
            result += 1
    return result

def fermat_theorem(a, p):
    return pow(a, p-1, p)

def euler_theorem(a, n):
    return pow(a, phi(n), n)

n = int(input("Enter a number: "))
a = int(input("Enter a base: "))
print(f"Euler’s Totient Function: {phi(n)}")
print(f"Fermat’s Theorem: {fermat_theorem(a, n)}")
print(f"Euler’s Theorem: {euler_theorem(a, n)}")
