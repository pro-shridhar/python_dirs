def binary_con(num: int) -> str:
    ans = ""
    while num > 0:
        rem = num % 2
        ans = str(rem) + ans
        num = num // 2

    return ans


num = int(input("give me a number = "))
print(binary_con(num))
