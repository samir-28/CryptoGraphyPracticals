from Crypto.Cipher import AES
from os import urandom

# Function to simulate S-Box substitution using AES encryption
def s_box_substitution(byte):
    key = b"\x00" * 16  # Using an all-zero key for consistency
    cipher = AES.new(key, AES.MODE_ECB)  # AES in ECB mode for single block encryption
    input_block = bytes([byte] + [0] * 15)  # 16-byte block with `byte` in the first position
    output_block = cipher.encrypt(input_block)  # Encrypt the block
    return output_block[0]  # Extract first byte as a substitute for S-Box lookup

# Function to generate a random 16-byte AES key
def generate_key():
    return urandom(16)  # Secure random AES key

# Testing
byte = 0x53  # Example input byte
substituted_byte = s_box_substitution(byte)

print(f"Original Byte: {hex(byte)} -> S-Box Output: {hex(substituted_byte)}")
print(f"Generated Key: {generate_key().hex()}")

