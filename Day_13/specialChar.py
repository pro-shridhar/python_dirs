import re


s = "Data!@Science#Rocks123"
res = re.sub(r"[^a-zA-Z]", "", s)
print(res)
