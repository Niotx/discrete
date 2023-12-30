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
    print('IRL', arr0[::-1])
    print('P', arr0)
    return arr0


def cut(arr):
    num = len(arr)
    flag = 0
    if num != 0:
        for i in range(num-1, -1, -1):
            if arr[i] == 1:
                flag = i
                break
            else:
                del arr[i]
    else:
        print(arr)
    return arr


def add(arr1, arr2):
    num = 0
    carry = 0
    addarr = []
    newadd = []
    if len(arr1) > len(arr2):
        num = len(arr1) - len(arr2)
        for i in range(num):
            arr2.append(0)
        for j in range(len(arr2)):
            if (arr1[j] + arr2[j] + carry) == 1:
                carry = 0
                addarr.append(1)
                newadd.append(2 ** j)
            elif (arr1[j] + arr2[j] + carry) == 2:
                carry = 1
                addarr.append(0)
                newadd.append(0)
                if len(arr2) == j + 1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
            elif (arr1[j] + arr2[j] + carry) == 0:
                carry = 0
                addarr.append(0)
                newadd.append(0)
            elif (arr1[j] + arr2[j] + carry) == 3:
                carry = 1
                addarr.append(1)
                newadd.append(2 ** j)
                if len(arr2) == j+1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
        # print('aad: ', newadd)
        # print('aad IRL: ', newadd[::-1])
    elif len(arr1) < len(arr2):
        num = len(arr2) - len(arr1)
        for i in range(num):
            arr1.append(0)
        for j in range(len(arr2)):
            if (arr1[j] + arr2[j] + carry) == 1:
                carry = 0
                addarr.append(1)
                newadd.append(2 ** j)
            elif (arr1[j] + arr2[j] + carry) == 2:
                carry = 1
                addarr.append(0)
                newadd.append(0)
                if len(arr2) == j + 1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
            elif (arr1[j] + arr2[j] + carry) == 0:
                carry = 0
                addarr.append(0)
                newadd.append(0)
            elif (arr1[j] + arr2[j] + carry) == 3:
                carry = 1
                addarr.append(1)
                newadd.append(2 ** j)
                if len(arr2) == j+1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
        # print('aad: ', newadd)
        # print('aad IRL: ', newadd[::-1])
    else:
        num = len(arr2) - len(arr1)
        for i in range(num):
            arr1.append(0)
        for j in range(len(arr2)):
            if (arr1[j] + arr2[j] + carry) == 1:
                carry = 0
                addarr.append(1)
                newadd.append(2 ** j)
            elif (arr1[j] + arr2[j] + carry) == 2:
                carry = 1
                addarr.append(0)
                newadd.append(0)
                if len(arr2) == j + 1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
            elif (arr1[j] + arr2[j] + carry) == 0:
                carry = 0
                addarr.append(0)
                newadd.append(0)
            elif (arr1[j] + arr2[j] + carry) == 3:
                carry = 1
                addarr.append(1)
                newadd.append(2 ** j)
                if len(arr2) == j+1:
                    addarr.append(1)
                    newadd.append(2 ** (j + 1))
        # print('aad: ', newadd)
        # print('aad IRL: ', newadd[::-1])
    return addarr


def multiplier(arr1, arr2):
    multi = []
    suma = []
    counter = 0
    for i in arr2:
        for h in range(counter):
            multi.append(0)
        for j in arr1:
            multi.append(j * i)
        suma = add(suma, multi)
        multi = []
        counter += 1
    return cut(suma)


while True:
    firstInp = int(input("Enter first decimal number : "))
    secondInp = int(input("Enter second decimal number : "))
    num1 = firstInp
    num2 = secondInp
    firstInp = binary(firstInp)
    secondInp = binary(secondInp)
    print('F:', firstInp, '\nF:', secondInp)
    firstInp = cut(firstInp)
    secondInp = cut(secondInp)
    addition = add(firstInp, secondInp)
    print(f'SUM: {num1+num2}=>', ':', addition[::-1])
    mul = multiplier(firstInp, secondInp)
    print(f'MUL: {num1*num2}=>', mul[::-1])
