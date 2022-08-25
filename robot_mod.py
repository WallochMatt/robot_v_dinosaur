from weaponr_mod import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("name", 00) #string, int
    
    def attack(self, dinosaur): #void: no return
        dinosaur.health = -self.active_weapon.attack_power #subtract the weapon's attack power from the dinsaur hp
