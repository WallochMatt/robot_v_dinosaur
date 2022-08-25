from weaponr_mod import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon_choices = [Weapon("Blaster Shot", 10), Weapon("Rocket", 30), Weapon("Sonic Blast", 20)]
        self.active_weapon = random.choice(self.weapon_choices)
        #^^This is the main editing point for this branch
    
    def attack(self, dinosaur): #void: no return
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power #subtract the weapon's attack power from the dinsaur hp
