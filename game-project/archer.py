from Champion import champion
import random

class archer(champion):
    def __init__(self,name,  health = 15, power = 10):
        self.health = health
        self.power = power
        self.name = name
        self.winphrase = " You shoot the enemy in the head instantly killing them, but why not double tap, so you shoot them in the heart too."

    def attack(self, enemy):
        power = self.power
        double_damage = random.randint(1, 101)
        if double_damage > 80:
            self.power = self.power * 2
            print("Critical Hit!")
        super().attack(enemy)
        self.power = power