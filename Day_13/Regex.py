import re

stng = "my roommate name is Aryan Sharma or (aloo)his EMAIL, is arsharma@bestpeers.com his: PHONE number; is 4564885693 ,3513452245134"
p1 = r"\b\d{10}\b"
p2 = r"\(\d{4}\)+\d{6}"  # (4564)885693
p3 = r"[A-Z]{1}[a-z]+"
p4 = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
p5 = r"[A-Za-z0-9._]+"
find = re.findall(p1, stng)
print(find)

email = "app@gmail.com"
mat = re.search(p4, email)
# print(mat.string)
print(mat.span())
