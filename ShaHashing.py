import hashlib

# Function to compute SHA-256 hash
def sha256_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()

# Function to compute SHA-512 hash
def sha512_hash(message):
    sha512 = hashlib.sha512()
    sha512.update(message.encode('utf-8'))
    return sha512.hexdigest()

# Main program
if __name__ == "__main__":
    message = input("Enter a message to hash: ")

    print("SHA-256 Hash:", sha256_hash(message))
    print("SHA-512 Hash:", sha512_hash(message))
