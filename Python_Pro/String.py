a = "Bestpeers"
print(a[0:3])

for i in a:
    print(i, end="")
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
if "in" not in txt:
    print("yes")
else:
    print("no")

str = "i am employee".replace("i am", "you are").split()
print(str, type(str))
