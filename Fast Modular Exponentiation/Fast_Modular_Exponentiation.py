def fast_modular_exponentiation(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2

    return result


while True:
    base = int(input('base: '))
    exponent = int(input('exponent: '))
    modulus = int(input('modulus: '))
    result = fast_modular_exponentiation(base, exponent, modulus)
    print(f"{base}^{exponent} mod {modulus} ≡", result)
