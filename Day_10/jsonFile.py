import json


with open("good.json", "r+") as file:
    read = file.read()
    print(read)

# data_to_write = {"city": "London", "population": 233463454}

# json_string = json.dumps(data_to_write, indent=2)

# with open("good.json", "a+") as json_file:
#     json_file.write(json_string)

# print("Data successfully written to city_data.json")
