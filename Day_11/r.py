import random

# Without setting a seed, the output will likely differ on each run
print("Without seed:")
print(random.random())
print(random.randint(1, 10))

# Setting a seed ensures reproducible results
random.seed(42)  # Using 42 as the seed
print("\nWith seed 42 (first run):")
print(random.random())
print(random.randint(1, 10))

random.seed(42)  # Using the same seed again
print("\nWith seed 42 (second run):")
print(random.random())
print(random.randint(1, 10))
