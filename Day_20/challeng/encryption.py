diss = {"a": 0, "e": 1, "i": 2, "o": 2, "u": 3}


def encrypt(word):
    string = ""
    for i in word:
        if i in "aeiou":
            string = str(diss[i]) + string
        else:
            string = i + string

    return string + "aca"


print(encrypt("banana"))
