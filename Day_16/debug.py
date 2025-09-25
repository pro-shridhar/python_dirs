import pdb


rows = 5


for i in range(1, rows + 1):
    # breakpoint()
    pdb.set_trace()
    for j in range(rows, i, -1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()
