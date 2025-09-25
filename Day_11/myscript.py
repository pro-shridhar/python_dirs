import csv

# with open("insurance.csv", "r") as csvfile:
#     reader_csv = csv.DictReader(csvfile, delimiter=",")
#     for line in reader_csv:
#         print(line)


with open("insurance.csv", "r") as csvfile:
    with open("new_insurance1.csv", "w") as csv_write:
        reader_csv = csv.reader(csvfile, delimiter=",")

        csv_writer = csv.writer(csv_write)

        # Writing Row by row
        for line in reader_csv:
            csv_writer.writerow(line)
