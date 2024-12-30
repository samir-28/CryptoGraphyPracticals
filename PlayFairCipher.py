import string

def prepare_matrix(key):
   # Prepare a 5x5 Playfair cipher matrix.
    key = key.upper().replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = list(dict.fromkeys(key + alphabet))  # Remove duplicates while preserving order
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def format_text(text):
    """Format text for Playfair cipher."""
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))  # Remove non-alphabetic characters
    result = []

    for i in range(0, len(text), 2):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result.extend([text[i], 'X'])
        else:
            result.append(text[i])
            if i + 1 < len(text):
                result.append(text[i + 1])

    if len(result) % 2 != 0:
        result.append('X')  # Add filler 'X' if odd length

    return ''.join(result)


def playfair_encrypt(text, matrix):
    """Encrypt text using Playfair cipher."""
    pos = {char: (row, col) for row, line in enumerate(matrix) for col, char in enumerate(line)}
    encrypted = []

    for i in range(0, len(text), 2):
        r1, c1 = pos[text[i]]
        r2, c2 = pos[text[i + 1]]

        if r1 == r2:  # Same row
            encrypted.append(matrix[r1][(c1 + 1) % 5])
            encrypted.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:  # Same column
            encrypted.append(matrix[(r1 + 1) % 5][c1])
            encrypted.append(matrix[(r2 + 1) % 5][c2])
        else:  # Rectangle
            encrypted.append(matrix[r1][c2])
            encrypted.append(matrix[r2][c1])

    return ''.join(encrypted)


def main():
    key = input("Enter the key: ")
    text = input("Enter the text: ")

    matrix = prepare_matrix(key)
    formatted_text = format_text(text)

    print("Playfair Cipher Matrix:")
    for row in matrix:
        print(" ".join(row))

    encrypted_text = playfair_encrypt(formatted_text, matrix)
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    main()
