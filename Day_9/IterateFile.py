import os

# Assign directory
directory = r"/home/developer/Desktop/Code_File/Day_9"

# Iterate over files in directory
for name in os.listdir(directory):
    print(f"Content of '{name}'")
    # Open file
    # with open(os.path.join(directory, name)) as f:
    #     print(f"Content of '{name}'")
    # Read content of file
    # print(f.read())

    print()
