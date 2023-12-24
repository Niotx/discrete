from math import sqrt as R

#
# def binary(num):
#     arr0 = []
#     numm = int(num)
#     new = 0
#
#     while numm < 0:
#         if num % 2 == 0:
#             arr0[new] = 0
#         if num % 2 == 1:
#             arr0[new] = 1
#         num = num / 2
#         new = new + 1
#         numm = numm - 1
#         print(numm)
#     #print(arr0)


first = int(input("Enter first decimal number : "))
second = int(input("Enter second decimal number : "))
radical1 = int(R(first)) + 1
radical2 = int(R(second)) + 1
#binary(first)
arr0 = []
numm = int(first)
new = radical1

while new > 0:
    if (first % 2) == 0:
        arr0.append(0)
    elif (first % 2) == 1:
    # if first % 2 == 1:
        arr0.append(1)
    first = first / 2
    new = new - 1
    print(new)
print(arr0)

