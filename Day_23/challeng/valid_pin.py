def valid(txt):

    if not txt.isnumeric() or " " in txt:
        print("1")
        return False

    if len(txt) != 4 and len(txt) != 6:
        print("2")
        return False

    return True


print(valid("123456"))
ans = "353".isnumeric()
print(ans)
