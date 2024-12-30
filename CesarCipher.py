import string

def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

# Input from user
text = input("Enter a string: ")
shift = int(input("Enter shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)
