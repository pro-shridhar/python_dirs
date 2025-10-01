import math

prime = [2]


def infinity():
    num = 3
    while True:
        yield num
        num += 1


def is_prime(num):
    limit = math.isqrt(num)
    for prime_num in prime:
        if prime_num > limit:
            break
        if num % prime_num == 0:
            return False
    prime.append(num)
    return True


for num in range(3, 1000):
    if is_prime(num):
        print(num)
