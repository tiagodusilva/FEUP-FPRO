import json

data = dict()
data[0] = 1
data[1] = 1

file_path = "\~Fibonaci_dictionary.json"

with open(file_path, 'w') as outfile:
    json.dump(data, outfile)
