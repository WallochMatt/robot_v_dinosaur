from robot_mod import Robot
from dinosaur_mod import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Domo")
        self.dinosaur = Dinosaur("RAAAGH", 25)#dino name and damage(attack power) 
        #self.robot_2 = Robot("CL4P")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        # ?: running the methods below in here 

    def display_welcome(self):
        print("WELCOME TO DINOSAUR LASER FIGHT")
        #add user friendly interface

    def battle_phase(self):
        while (self.robot.health > 0)  and (self.dinosaur.health > 0):
        #if self.robot.health or self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            #input("Enter: Next turn")
            self.dinosaur.attack(self.robot)
            #input("Enter: Next turn")
        # ?: run the math for the fighting

    def display_winner(self):
        if self.robot.health <= 0:
            print(f"{self.dinosaur.name} wins!")
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} wins!")
            
    # ?: if x healt = 0, print the opposite win, so if dino.hp = 0 then robot wins

# dino_test = Dinosaur("Test", 50)
# robo_test = Robot("T35T")

# robo_test.attack(dino_test)