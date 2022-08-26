
from fleet_mod import Fleet
from herd_mod import Herd

import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("WELCOME TO DINOSAUR LASER FIGHT")


    def battle_phase(self):
        while len(self.fleet.list_robo) > 0 and len(self.herd.list_dino)> 0:

            self.current_robot = random.choice(self.fleet.list_robo)
            self.current_dino = random.choice(self.herd.list_dino)
            
            self.current_robot.attack(self.current_dino)
            
            print(f"{self.current_dino.name} took {self.current_robot.active_weapon.attack_power} damage! \n {self.current_dino.name} has {self.current_dino.health} HP left!")
            
            for d in self.herd.list_dino:
                if (d).health <= 0:
                    self.herd.list_dino.remove(d) #print d has fallen
                    print(f"{(d).name} has fallen!!")

            self.current_dino.attack(self.current_robot)
            
            print(f"""{self.current_robot.name} took {self.current_dino.attack_power} damage! \n {self.current_robot.name} has {self.current_robot.health} HP left!""")

            for r in self.fleet.list_robo:
                if (r).health <= 0:
                    self.fleet.list_robo.remove(r)
                    print(f"{(r).name} has fallen!!")
            input("Next Round!: Enter")
            
    def display_winner(self):
        if len(self.fleet.list_robo) == 0:
            print("\n DINOS WIN")
        if len(self.herd.list_dino) == 0:
            print("\n ROBOTS WIN")