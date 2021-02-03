from Champion import champion
import random

class mage(champion):
    def __init__(self,name, health = 15, power = 10):
        self.health = health
        self.power = power
        self.name = name
        self.winphrase = "You charge up your spell and blast the enemy into pieces, blood and flesh flies everywhere."
    
    def attack(self, enemy):
        power = self.power
        double_damage = random.randint(1, 101)
        if double_damage > 80:
            self.power = self.power * 2
            print("Critical Hit!")
        super().attack(enemy)
        self.power = power