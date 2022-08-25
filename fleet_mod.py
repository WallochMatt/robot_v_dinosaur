from robot_mod import Robot
import random

class Fleet:
    def __init__(self):
        self.list = [Robot("Domo"), Robot("Arigato"), Robot("Mr. Roboto")]
        self.choice = random.choice(self.list)