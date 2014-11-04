class Hero(Entity):

    #max_health = 100

    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname

    def known_as(self):
        alias = self.name + " the " + self.nickname
        return alias

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points
        return self.health

    def take_healing(self, healing_point):
        if self.health == 0:
            return False
        elif self.health + healing_point > 100:
            self.health = 100
        else:
            self.health = self.health + healing_point
        return self.health

h = Hero("Bron", 100, "DragonSlayer")
print(h.known_as())
