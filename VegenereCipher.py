def vigenere_encrypt(text, key):
    """Encrypt text using the Vigenère cipher."""
    text = text.upper().replace(" ", "")
    key = (key.upper() * ((len(text) // len(key)) + 1))[:len(text)]  # Repeat the key to match text length
    encrypted = [(ord(t) + ord(k) - 2 * ord('A')) % 26 + ord('A') for t, k in zip(text, key)]
    return ''.join(map(chr, encrypted))


def main_vigenere():
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    encrypted_text = vigenere_encrypt(text, key)
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    print("Vigenère Cipher")
    main_vigenere()
