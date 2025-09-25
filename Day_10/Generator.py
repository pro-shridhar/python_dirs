# def cvs(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result


# print(cvs("techcrunch.csv"))

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"""

# csv_gen = open("techcrunch.csv")
# row_count = 0

# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"""

# file_name = "techcrunch.csv"
# csv_gen = (row for row in open(file_name))
# print(csv_gen)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"""

# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         print(row)
#         yield row


# file_name = "techcrunch.csv"
# # Consume the generator
# for line in csv_reader(file_name):
#     pass  # or process each line

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"""


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")

"""Instead, the state of the function is remembered.
That way, when next() is called on a generator object
(either explicitly or implicitly within a for loop),
the previously yielded variable num is incremented, and
then yielded again."""

gen = infinite_sequence()
print(next(gen))
print(next(gen))
