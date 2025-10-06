import re

string = "I went to him at 11 A.M. on 4th July 1886"

new = re.sub("\d", "0", string)
print(new)
