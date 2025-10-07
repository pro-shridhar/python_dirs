def k_th_binary_inlist(n, k):

    n = (2**n) - 1

    ds = []
    for i in range(n + 1):

        ds.append((str(bin(i))))
    print(ds)

    lst = sorted(ds, key=lambda x: (x.count("1")), reverse=True)

    return lst[k - 1]


# ["0b111", "0b11", "0b101", "0b110", "0b1", "0b10", "0b100", "0b0"]
# ["0b1111", "0b111", "0b1011", "0b1101", "0b1110", "0b11",
#  "0b101", "0b110", "0b1001", "0b1010", "0b1100", "0b1", "0b10",
# "0b100", "0b1000", "0b0"]
