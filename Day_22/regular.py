import re

string = "I went to him at 11 A.M. on 4th July 1886"

rc = re.compile("\d+")
strf = rc.findall(string)
print(strf)
