def to_binary(num):
    binary = bin(num)
    return binary[2:]


print(to_binary(0xFF))
