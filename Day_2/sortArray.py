a = 13
b = 8

print(a | b)
print(a & b)
print(~a)
print(a ^ b)
print(4 << 2)  # 4 * 2^2
print(4 >> 2)  # 4 / 2^2


"""
  1101
  1000"""

list = [2, 3, 8, 4, 6]
tuple = (3, 6, 2, 48, 6)
set = {3, 7, 3, 8}
dics = {"name": "anurag", "mark": 94}


print(list, type(list))
print(tuple, type(tuple))
print(set, type(set))
print(dics, type(dics))

c = "abc"
d = "def"
c, d = d, c
print(c, d)
