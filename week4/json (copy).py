import json
from pprint import pprint


class JsonWriter():

    def __init__(self, species, name, age, weight):
        self.species = species
        self.name = name
        self.age = age
        self.weight = weight

    def write(self):
        data = {"species": self.species, "name": self.name, "age": self.age, "weight": self.weight}
        with open('json_data.json', 'w') as json_file:
                json.dump(data, json_file)

zoo = JsonWriter("tiger", "ani", 2, 32)
zoo1 = JsonWriter("bear", "geri", 4, 15)
zoo2 = JsonWriter("dog", "erin", 5, 76)
zoo.write()
zoo1.write()
jdata = json.load(open('json_data.json'))
pprint(jdata)
