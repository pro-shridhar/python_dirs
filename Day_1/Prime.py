def prime(num: int):

    if num == 2:
        print("this number is prime number")
    elif num < 2:
        print("give me number greater then 2")

    number = int(num / 2)
    for i in range(3, number):
        if num % i == 0:
            print("not a prime number")
    print("this number is prime number")


prime(37)
