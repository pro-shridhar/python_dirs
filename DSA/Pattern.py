rows = 5  # Number of rows for the triangle

for i in range(rows + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for printing stars
        print("* ", end="")
    print()  # Move to the next line after each row

print("\n")

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i, rows + 1):  # Inner loop for printing stars
        print("* ", end="")
    print()  # Move to the next line after each row

print("\n")

for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()
