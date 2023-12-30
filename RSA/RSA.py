def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def fast_modular_exponentiation(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    p = int(input("Enter the value of p: "))
    q = int(input("Enter the value of q: "))
    e = int(input("Enter the value of e: "))
    if not is_prime(p) or not is_prime(q):
        print("Both p and q should be prime numbers.")
        return
    n = p * q
    if gcd(e, (p - 1) * (q - 1)) != 1:
        print("gcd(e, (p-1)(q-1)) should be 1.")
        return
    sentence = input("Enter an English sentence: ")
    encrypted_sentence = ""
    for char in sentence:
        ch = char.upper()
        if 'A' <= ch <= 'Z':
            num_value = ord(ch) - ord('A')
            encrypted_sentence += str(fast_modular_exponentiation(num_value, e, n)) + " "
    print("Encrypted sentence:", encrypted_sentence.strip())


if __name__ == "__main__":
    while True:
        main()
