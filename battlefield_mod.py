from robot_mod import Robot
from dinosaur_mod import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Named Robt")
        self.dinosaur = Dinosaur("Raaagh", 25)#dino name and damage(attack power) 
        #self.robot_2 = Robot("CL4P")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        # ?: running the methods below in here 

    def display_welcome(self):
        print("WELCOME TO DINOSAUR LASER FIGHT")
        #add user friendly interface

    def battle_phase(self):
        while (self.robot.health > 0)  or (self.dinosaur.health > 0):
        #if self.robot.health or self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            #input("Enter: Next turn")
            self.dinosaur.attack(self.robot)
            #input("Enter: Next turn")
        # ?: run the math for the fighting

    def display_winner(self):
        pass
    # ?: if x healt = 0, print the opposite win, so if dino.hp = 0 then robot wins

# dino_test = Dinosaur("Test", 50)
# robo_test = Robot("T35T")

# robo_test.attack(dino_test)