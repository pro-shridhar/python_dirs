word1 = "listen"
word2 = "silent"

obj = {}
for i in word2:
    if i in obj.keys():
        obj[i] = obj[i] + 1
    else:
        obj[i] = 1

print(obj)

for char in word1:
    if char not in obj:
        print("not a anagram")
        break
    else:
        obj[char] -= 1


print(obj)
