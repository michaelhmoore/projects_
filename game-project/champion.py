from Champion import champion
import random

class fighter(champion):
    def __init__(self,name,health = 25, power = 9,):
        self.health = health
        self.power = power
        self.name = name
        self.winphrase = "You slice the enemy down the middle of their body in one clean swoop of your blade"
    
    def attack(self, enemy):
        power = self.power
        double_damage = random.randint(1, 101)
        if double_damage > 80:
            self.power = self.power * 2
            print("Critical Hit!")
        super().attack(enemy)
        self.power = power