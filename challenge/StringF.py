def formatString(string: str) -> str:
    string = string.replace(".", " ")
    return f"\"<{string[0]} class='{string[2:]}'></{string[0]}>\""


# "<p class='one'></p>"

string = input("give a string = ")
print(formatString(string))
