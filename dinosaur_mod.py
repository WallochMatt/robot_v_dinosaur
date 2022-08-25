class Dinosaur:
    def __init__(self, name, attack_power): #may change to attack strength to avoid confusion
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):#void
        robot.health = robot.health - self.attack_power
