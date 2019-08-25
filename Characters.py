from Items import *
from World import *
import curses
from Encounters import *
from random import randint
import math


class BaseCharacter:

    def __init__(self, health, weapon, strength):
        self.health = health
        self.equipped_weapon = weapon
        self.rations = Ration(2000)
        self.bandages = Bandage(0)
        self.strength = strength

    def attack(self):
        return self.equipped_weapon.damage

    def heal(self):
        self.health += self.bandages.use_bandage()

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


class Player(BaseCharacter):

    def __init__(self, location):
        super(Player, self).__init__(100, Fist(), 10)
        self.name = ""
        self.location = location
        self.coins = 0
        self.experience = 0

    def travel(self, y_change, x_change,  world_map):
        if world_map.is_valid_move(self.location, world_map, y_change, x_change):   # if move is okay
            if self.rations.eat_ration():   # if player has enough rations
                self.location = world_map.map_grid[self.location.y + y_change][self.location.x + x_change]  # travel
                self.experience += 1

    def add_rations(self, num_to_add):
        self.rations.quantity += num_to_add

    def run_away(self):
        return True


class Bandit(BaseCharacter):

    def __init__(self, experience):
        super(Bandit, self).__init__(100, Fist(), 10)

        random_number = randint(1, 9)

        if (experience/10*random_number) < 200:
            self.equipped_weapon = Fist()
        elif (experience/10*random_number) < 400:
            self.equipped_weapon = Cudgel()
        elif (experience/10*random_number) < 800:
            self.equipped_weapon = Knife()
        elif (experience/10*random_number) < 1600:
            self.equipped_weapon = Spear()
        elif (experience/10*random_number) < 3200:
            self.equipped_weapon = Sword()

        self.health = math.ceil(randint(2, 6) * (experience/100 + 1))
        self.bandages = Bandage(randint(0, 4))


class Wizard:

    def __init__(self, location):
        self.location = location

    def travel(self, new_location, world_map):
        if world_map.is_valid_move(new_location, world_map, 0, 0):
            self.location = new_location


# class Bear(BaseCharacter):
# class Trader(BaseCharacter):
