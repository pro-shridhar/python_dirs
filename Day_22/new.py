def censor_string(txt, lst, char):

    for i in lst:
        i = i.lower()
        j = i.title()
        if i in txt or j in txt:
            if j in txt:
                txt = txt.replace(j, len(j) * char)

            txt = txt.replace(i, len(i) * char)

    return txt
