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
    #print(arr0[::-1])
    print('*', arr0)
    #print(len(arr0))
    return arr0


def cut(arr):
    num = len(arr)
    flag = 0
    if num != 0:
        for i in range(num-1, -1, -1):
            #print('*', i)
            if arr[i] == 1:
                flag = i
                break
            else:
                del arr[i]
        # print(flag, arr)
    else:
        print(arr)
# def compare(arr1, arr2):
#     if len(arr1) > len(arr2):


firstInp = int(input("Enter first decimal number : "))
secondInp = int(input("Enter second decimal number : "))
binary(firstInp)
binary(secondInp)
cut(binary(firstInp))

