import numpy as np

def hill_encrypt(text, key_matrix):
    """Encrypt text using the Hill cipher."""
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'  # Add filler if text length is odd

    pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
    encrypted = ""
    for pair in pairs:
        vector = np.array([ord(pair[0]) - ord('A'), ord(pair[1]) - ord('A')])
        result = np.dot(key_matrix, vector) % 26
        encrypted += ''.join(chr(val + ord('A')) for val in result)

    return encrypted


def main_hill():
    text = input("Enter the text: ")
    key_matrix = np.array([[3, 6], [1, 5]])  # Example 2x2 matrix; replace as needed
    encrypted_text = hill_encrypt(text, key_matrix)
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    print("Hill Cipher")
    main_hill()
