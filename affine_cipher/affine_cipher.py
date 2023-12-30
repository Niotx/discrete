def affine_encrypt(sentence, a, b):
    encrypted = ""
    for char in sentence:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted


def affine_decrypt(encrypted_sentence, a, b):
    decrypted = ""
    a_inverse = next((j for j in range(26) if (a * j) % 26 == 1), 0)
    for char in encrypted_sentence:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - b) * a_inverse) % 26 + ord('A'))
                if decrypted_char < 'A':
                    decrypted_char += 26
            else:
                decrypted_char = chr(((ord(char) - ord('a') - b) * a_inverse) % 26 + ord('a'))
                if decrypted_char < 'a':
                    decrypted_char += 26
            decrypted += decrypted_char
        else:
            decrypted += char
    return decrypted


def main():
    sentence = input("Enter a sentence: ")
    operation = input("What do you want (Encrypt/Decrypt): ").capitalize()
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    if operation == "Encrypt":
        result = affine_encrypt(sentence, a, b)
        print("Encrypted sentence:", result)
    elif operation == "Decrypt":
        result = affine_decrypt(sentence, a, b)
        print("Decrypted sentence:", result)
    else:
        print("Error: Invalid operation.")


if __name__ == "__main__":
    main()
