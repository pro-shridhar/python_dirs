import math


def line_length(dot1, dot2):
    return round(math.sqrt((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2), 2)


print(line_length([0, 0], [0, 0]))
