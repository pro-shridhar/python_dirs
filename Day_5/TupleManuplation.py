# but they can contain mutable objects string:
# also immutable therefor in string excaption
# v = ("Anurodh", [3, 2, 1])
# print(v[0][1])
# v[0][1] = 5
# print(v[0][1])


# arr = ["Appu", "Aman"]
# list1 = ["a", "b"]
# list2 = list("Appu") to convert list of string to char array
# print(arr, "\n", list1, "\n", list2)

empty = ()
singleton = ("hello",)  # <-- note trailing comma
print(len(empty))

print(len(singleton))

print(singleton)
