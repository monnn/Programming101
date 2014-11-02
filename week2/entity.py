from random import randint


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health

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
        max_health = 100
        if self.health == 0:
            return False
        elif self.health + healing_point > max_health:
            self.health = max_health
        else:
            self.health = self.health + healing_point
        return self.health

    def has_weapon(self):
        return False

    def equip_weapon(self, weapon):
        #equips the given weapon to the entity
        return 0

    def attack(self):
        #return the damage, that the given Entity is doing. If the entity has no weapon, the damage is 0
        return 0


class Hero(Entity):

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        alias = self.name + " the " + self.nickname
        return alias

h = Hero("Bron", 100, "DragonSlayer")
print(h.known_as())
print(h.get_health())


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        if berserk_factor > 2:
            berserk_factor = 2
        elif berserk_factor < 1:
            berserk_factor = 1
o = Orc("frf", 89, 3)
print(o.get_health())


class Weapon:
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if self.critical_strike_percent < 0.5:
            return True
        else:
            return False


class Fight:
    def __init__(self, hero, orc):
        self.hero = Hero
        self.orc = Orc
        #if hero is Hero and orc is Orc:
        happy_number = randint(0, 100)
        if happy_number < 50:
            hero.attack()
        else:
            orc.attack()

    def simulate_fight(self):
        print(self.hero.get_health())
        print(self.orc.get_health())

class Dungeon:
    def __init__(self, filename):
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()