def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def chinese_equations(mods, nums, n):
    multipl_mod = 1
    for i in range(n):
        multipl_mod *= mods[i]

    result = 0
    for j in range(n):
        M_k = multipl_mod // mods[j]
        result += nums[j] * mod_inverse(M_k, mods[j]) * M_k
    return result % multipl_mod


def main():
    n = int(input("Enter the number of equations: "))
    mods = []
    nums = []
    for i in range(n):
        mods.append(int(input(f"mod {i + 1}: ")))
        nums.append(int(input(f"a {i + 1}: ")))
    result = chinese_equations(mods, nums, n)
    print("answer:", result)


if __name__ == "__main__":
    while True:
        main()
