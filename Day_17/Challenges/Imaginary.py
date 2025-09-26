def interview(lst, tot):
    limits = [5, 5, 10, 10, 15, 15, 20, 20]

    if len(lst) != 8:
        return "disqualified"

    for t, limit in zip(lst, limits):
        if t > limit:
            return "disqualified"

    if tot > 120:
        return "disqualified"

    return "qualified"
