import pickle

# First, save some data to a file
my_data = {"name": "Alice", "age": 30}
with open("data.pkl", "wb") as file:
    pickle.dump(my_data, file)

# Then, load the data back from the file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# Output: {'name': 'Alice', 'age': 30}
