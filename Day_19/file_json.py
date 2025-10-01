import json


def read_json():
    with open("good.json", "r") as json_f:
        file = json.load(json_f)
        for line in file:
            yield line


content = read_json()
for line in content:
    print(line)
