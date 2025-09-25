def fun(num1: int, num2: int):

    prime_number = []
    for i in range(num1, num2 + 1):
        if num1 < 1:
            continue
        elif i > 2:
            half = i // 2
            for j in range(2, half + 1):
                if i % j == 0:
                    break
                elif j == half:
                    prime_number.append(i)
        elif i == 2:
            prime_number.append(i)
        else:
            continue

    print("amstrongNumber = ", prime_number)

    amstrong_number = []
    for i in range(num1, num2 + 1):
        string = str(i)
        sum = 0
        for j in string:
            if num1 < 1:
                continue
            curr_int = int(j)
            sum += curr_int**3
        if sum == i:
            amstrong_number.append(i)

    print("amstrongNumber = ", amstrong_number=[])


fun(131, 378)
