from robot_mod import Robot
from dinosaur_mod import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Named Robt")
        self.dinosaur = Dinosaur("Raaagh", 25)#dino name and damage(attack power) 

    def run_game(self):
        pass # ?: running the methods below in here 

    def display_welcome(self):
        pass #add user friendly interface

    def battle_phase(self): 
        pass # ?: run the math for the fighting

    def display_winner(self):
        pass
    # ?: if x healt = 0, print the opposite win, so if dino.hp = 0 then robot wins

dino_test = Dinosaur("Test", 50)
robo_test = Robot("T35T")

robo_test.attack(dino_test)