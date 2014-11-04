class orc:

    #max_health = 100

    def __init__(self, name, health, berserk_factor):
        self.name = name
        self.health = health
        self.berserk_factor = berserk_factor
        if berserk_factor > 2:
            berserk_factor = 2
        elif berserk_factor < 1:
            berserk_factor = 1

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

h = hero("Bron", 100, 1.2)
print(h.known_as())
