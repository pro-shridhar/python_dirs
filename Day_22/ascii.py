def to_dict(lst):
    ansl = []
    for i in lst:
        ans = {}
        ans[i] = int(ord(i))
        ansl.append(ans)

    return ansl


print(to_dict(["a", "b", "c"]))
