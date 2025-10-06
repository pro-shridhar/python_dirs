def fix_import(s):

    lst = s.split(" ")
    ans = " ".join(lst[2:]) + " " + " ".join(lst[:2])
    return ans


print(fix_import("import object from module_name"))
