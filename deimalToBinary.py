from math import sqrt as R


def binary(first):
    radical1 = int(R(first)) + 1
    if int(first) == 2 ** radical1:
        radical1 = radical1 + 1
    arr0 = []
    new = radical1
    while new > 0:

        if (first % 2) == 0:
            arr0.append(0)
        else:
            arr0.append(1)
        first = first / 2
        first = int(first)
        new = new - 1
    print(arr0[::-1])
    print('*', arr0)
    return arr0

firstInp = int(input("Enter first decimal number : "))
secondInp = int(input("Enter second decimal number : "))
binary(firstInp)
binary(secondInp)

