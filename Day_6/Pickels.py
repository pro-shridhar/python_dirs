import pickle

# A pickled object as a bytes string
my_data = {"name": "Bob", "city": "New York"}
pickled_bytes = pickle.dumps(my_data)

# The 'pickled_bytes' is now a bytes object, like this:
# b'\x80\x04\x95\x1e\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x04city\x94\x8c\x08New York\x94u.'

# Now, loads() can be used to deserialize the bytes string
loaded_data = pickle.loads(pickled_bytes)

# To identify the highest protocol that your interpreter supports,
print(pickle.HIGHEST_PROTOCOL)
print(loaded_data)
# Output: {'name': 'Bob', 'city': 'New York'}
