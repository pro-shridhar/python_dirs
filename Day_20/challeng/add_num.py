def add(n1, n2):
    if not n1 or not n2:
        return "Invalid Operation"

    return str(int(n1) + int(n2))


print(add("23", None))
