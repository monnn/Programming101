import json

from pprint import pprint
json_data = open('json_data.json')

data = json.load(json_data).read()
pprint(data)
json_data.close()