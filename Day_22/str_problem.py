import re

string = "Why did the chicken cross the road?"
slst = string.split(" ")
lst = ["Did", "chicken", "road"]
for i, s in enumerate(slst):
    curr = s.lower()
    cleaned = re.sub(r"\W", "", curr)
    schar = re.findall(r"\W", s)
    if cleaned in lst or cleaned.title() in lst:
        idx = 0
        if schar:
            idx = curr.index(schar[0])
            slst[i] = "-" * (idx) + schar[0]
        else:
            slst[i] = "-" * (len(slst[i]) - idx)
ans = " ".join(slst)
print(ans)

# import re

# # Input sentence
# sentence = "is this Very book is very nice book to read?"
# lst = ["very", "read"]

# # Use regular expression to split into words and special characters
# tokens = re.findall(r"\w+|[^\w\s]", sentence)

# for i, s in enumerate(tokens):
#     curr = s.lower()
#     if curr in lst:
#         tokens[i] = "-" * len(s)

# ans = " ".join(tokens)
# print(ans)
