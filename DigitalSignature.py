import hashlib

# Function to compute SHA-256 hash
def sha256_hash(message):
    sha256 = hashlib.sha256()  # Create a SHA-256 hash object
    sha256.update(message.encode('utf-8'))  # Update the hash with the message
    return sha256.hexdigest()  # Return the hash (digital fingerprint of the message)

# Main program
if __name__ == "__main__":
    message = input("Enter a message: ")
    
    # Compute the hash (which acts like a "signature")
    message_hash = sha256_hash(message)
    
    print("Message Hash (Digital Signature Simulation):")
    print(message_hash)
    
    # Simulating verification by hashing the message again and comparing
    verify_message = input("\nVerify the message by entering it again: ")
    
    # Hash the second message
    verify_hash = sha256_hash(verify_message)
    
    if verify_hash == message_hash:
        print("\n The message is valid and hasn't been altered.")
    else:
        print("\n The message has been altered.")
