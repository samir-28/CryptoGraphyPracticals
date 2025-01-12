class Polynomial:
    def __init__(self, coefficients, modulus=None):
        """
        Initialize a polynomial.
        :param coefficients: List of coefficients (from lowest to highest degree).
        :param modulus: Prime modulus for coefficients (None for no modular arithmetic).
        """
        self.coefficients = [coef % modulus if modulus else coef for coef in coefficients]
        self.modulus = modulus

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                term = f"{coef}" if i == 0 else (f"{coef}x^{i}" if i > 1 else f"{coef}x")
                terms.append(term)
        return " + ".join(terms[::-1]) if terms else "0"

    def add(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        self_coeff = self.coefficients + [0] * (max_len - len(self.coefficients))
        other_coeff = other.coefficients + [0] * (max_len - len(other.coefficients))
        result = [(self_coeff[i] + other_coeff[i]) % self.modulus if self.modulus else self_coeff[i] + other_coeff[i]
                  for i in range(max_len)]
        return Polynomial(result, self.modulus)

    def subtract(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        self_coeff = self.coefficients + [0] * (max_len - len(self.coefficients))
        other_coeff = other.coefficients + [0] * (max_len - len(other.coefficients))
        result = [(self_coeff[i] - other_coeff[i]) % self.modulus if self.modulus else self_coeff[i] - other_coeff[i]
                  for i in range(max_len)]
        return Polynomial(result, self.modulus)
  
    def multiply(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, self_coef in enumerate(self.coefficients):
            for j, other_coef in enumerate(other.coefficients):
                product = self_coef * other_coef
                if self.modulus:
                    product %= self.modulus
                result[i + j] += product
                if self.modulus:
                    result[i + j] %= self.modulus
        return Polynomial(result, self.modulus)

    def mod(self, modulus_poly):
        """
        Polynomial modulo operation.
        :param modulus_poly: Polynomial modulus for division.
        :return: Remainder of division.
        """
        remainder = self.coefficients[:]
        while len(remainder) >= len(modulus_poly.coefficients):
            lead_coeff = (
                remainder[-1] * pow(modulus_poly.coefficients[-1], -1, self.modulus)
                if self.modulus
                else remainder[-1] / modulus_poly.coefficients[-1]
            )
            lead_degree = len(remainder) - len(modulus_poly.coefficients)
            subtract_poly = [0] * lead_degree + [c * lead_coeff for c in modulus_poly.coefficients]
            if self.modulus:
                subtract_poly = [c % self.modulus for c in subtract_poly]
            remainder = [
                (a - b) % self.modulus if self.modulus else a - b
                for a, b in zip(remainder + [0] * (len(subtract_poly) - len(remainder)), subtract_poly)
            ]
            while remainder and remainder[-1] == 0:
                remainder.pop()
        return Polynomial(remainder, self.modulus)


# Example Usage
if __name__ == "__main__":
    prime_modulus = 7  # Example modulus for finite field
    p1 = Polynomial([1, 2, 3], modulus=prime_modulus)  # 1 + 2x + 3x^2 (mod 7)
    p2 = Polynomial([3, 1], modulus=prime_modulus)     # 3 + x (mod 7)
    modulus_poly = Polynomial([1, 0, 1], modulus=prime_modulus)  # x^2 + 1 (mod 7)

    print("Polynomial 1:", p1)
    print("Polynomial 2:", p2)
    print("Modulus Polynomial:", modulus_poly)

    # Addition
    add_result = p1.add(p2)
    print("Addition:", add_result)

    # Subtraction
    sub_result = p1.subtract(p2)
    print("Subtraction:", sub_result)

    # Multiplication
    mul_result = p1.multiply(p2)
    print("Multiplication:", mul_result)

    # Modulo Operation
    mod_result = p1.multiply(p2).mod(modulus_poly)
    print("Modulo Operation:", mod_result)
