import csv


def read_file():
    with open("techcrunch.csv", "r") as file:

        for line in csv.reader(file):
            yield line


content = read_file()
for i in content:
    print(i)
