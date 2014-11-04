class Zoo:
    import json
    from pprint import pprint

    def __init__(self, capacity):
        self.animals is Animal
        self.capacity = capacity
        self.daily_incomes = 0
        self.daily_outcomes = 0
        self.budget = 0
        #self.list_of_animals = open("json_data.txt").read()
        self.number_of_animals = 0

    def list_animals(self):
        json_data = open('json_data.txt').read()
        self.data = json.load(json_data)
        pprint(data)
        json_data.close()
        return self.data

    def accommodate(self, species, name, age, weight):
        data = {"species": self.species, "name": self.name, "age": self.age, "weight": self.weight}
        while self.number_of_animals < self.capacity:
            #self.list_of_animals.update({})
            with open('json_data.json', 'w') as outfile:
                json.dump(data, outfile)
            self.number_of_animals += 1

    def set_daily_incomes(self):
        pass

    def set_daily_outcomes(self):
        pass

    def get_budget(self):
        self.budget = self.get_daily_incomes() - self.get_daily_outcomes()
        return self.budget

    def move_to_habitat(self, species, name):
        pass

    def simulate(interval_of_time, period):
        pass
