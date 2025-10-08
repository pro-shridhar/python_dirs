def atbash(txt):

    for i in txt:
        if ord(i) > 64 and ord(i) < 91:
            txt = txt.replace(i, chr(91 - (ord(i) - 64)))

        txt = txt.replace(i, chr(122 - (ord(i) - 97)))

    print(txt)


atbash("Hello world!")
print(ord("A"), ord("Z"), ord("a"), ord("z"))
