def atbash(txt):

    for i in txt:

        txt = txt.replace(i, chr(122 - (ord(i) - 97)))

    print(txt)


atbash("Hello world!")
print(ord("A"), ord("Z"), ord("a"), ord("z"))
