import hashlib
from Crypto.Hash import MD4
# Function to compute MD4 hash
def md4_hash(message):
    md4 = MD4.new()
    md4.update(message.encode('utf-8'))
    return md4.hexdigest()

# Function to compute MD5 hash
def md5_hash(message):
    md5 = hashlib.md5()
    md5.update(message.encode('utf-8'))
    return md5.hexdigest()

# Main program
if __name__ == "__main__":
    message = input("Enter a message to hash: ")

    print("MD4 Hash:", md4_hash(message))
    print("MD5 Hash:", md5_hash(message))
