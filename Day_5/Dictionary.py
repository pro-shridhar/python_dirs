d = {1: "Geeks", 2: "For", 3: "Geeks"}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

print(d.pop("age"))

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")


d = {1: "Geeks", 2: "For", "age": 22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

d = {"a": 1, "b": 2}

# Adding a single key-value pair
d.update({"c": 3})

# Adding multiple key-value pairs
d.update({"d": 4, "e": 5})

print(d)

"""dictionary unpacking allows us to merge dictionaries or add new
 key-value pairs in a concise way. By using the unpacking operator
 **, we can merge an existing dictionary with new items in a single
 statement."""

d = {"key1": "geeks", "key2": "for"}

d = {**d, "key3": "Geeks", "key4": "is", "key5": "portal", "key6": "Computer"}
print(d)
print([(x, y) for x, y in d.items()])
