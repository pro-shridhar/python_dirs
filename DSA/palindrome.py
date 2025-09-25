def check(s):
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False

    return True


if check("nama"):
    print("is palindrome")
else:
    print("not a palindrome")
