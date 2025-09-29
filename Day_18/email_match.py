import re

email = input("give me a email ")
p1 = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
p2 = r"[+91][\d]{10}"

result = re.match(p1, email)
result = re.match(p2, email)
print(result)
