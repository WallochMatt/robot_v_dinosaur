from dinosaur_mod import Dinosaur
import random

class Herd:
    def __init__(self):
         self.list = [Dinosaur("RAAAGH", 20), Dinosaur("HHHIIIHKK", 15), Dinosaur("GGAAWR", "35")]
         self.choice = random.choice(self.list)