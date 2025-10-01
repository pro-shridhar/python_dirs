import csv


def read_file():
    with open("Day_11/insurance.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


# Create generator
content = read_file()

# Print each row as a dictionary
for row in content:
    print(row)
