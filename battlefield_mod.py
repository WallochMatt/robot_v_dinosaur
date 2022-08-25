from fleet_mod import Fleet
from herd_mod import Herd
#i dont know if choice should go in a method here or on fleet page

class Battlefield:
    def __init__(self):
      self.fleet = Fleet()
      self.herd = Herd()
        #^^^Random robot/dino in a list, targets another random?

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        #self.display_winner()
        # ?: running the methods below in here 

    def display_welcome(self):
        print("WELCOME TO DINOSAUR LASER FIGHT")
        #add user friendly interface

    # def selects_opponents(self):
    #     if self.fleet.health <= 0:
                #remove self.fleet
                #reroll

    def battle_phase(self):
        while (self.fleet.choice.health > 0)  and (self.herd.choice.health > 0): #while fleet and herd have values in the list?
        #if self.robot.health or self.dinosaur.health > 0:
            self.fleet.choice.attack(self.herd.choice)
           # input("Enter: Next turn")
            self.herd.choice.attack(self.fleet.choice)
            #input("Enter: Next turn")
        # ?: run the math for the fighting
            if self.fleet.choice.health < 0:
                self.fleet.list.remove(self.fleet.choice)#successfully removed robot from the list
                #make it reselct a new robot

            if self.herd.choice.health < 0:
                self.herd.list.remove(self.herd.choice)


    def display_winner(self):
        if self.robot.health <= 0:
            print(f"{self.dinosaur.name} wins!")
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} wins!")
            
    # ?: if x healt = 0, print the opposite win, so if dino.hp = 0 then robot wins

# dino_test = Dinosaur("Test", 50)
# robo_test = Robot("T35T")

# robo_test.attack(dino_test)