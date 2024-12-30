def rail_fence_encrypt(text, rails):
    """Encrypt text using the Rail Fence cipher."""
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1

    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(''.join(rail) for rail in fence)


def main_rail_fence():
    text = input("Enter the text: ")
    rails = int(input("Enter the number of rails: "))
    encrypted_text = rail_fence_encrypt(text, rails)
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    print("Rail Fence Cipher")
    main_rail_fence()
