import math


def frection_value(value):
    string = str(value)
    count = [x for x in range(len(string)) if string[x] == "."]
    count = count[0]
    deno = 10 ** (len(string) - count - 1)
    if int(string[count + 1 :]) == 0:
        raise ValueError("this is complete value")
    neno = int(string[:count] + string[count + 1 :])
    print(neno, deno)
    gcd = math.gcd(neno, deno)
    deno = deno // gcd
    neno = neno // gcd

    return "{}/{}".format(neno, deno)


# print(frection_value(23.345))
