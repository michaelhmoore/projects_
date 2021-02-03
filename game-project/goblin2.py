from Champion import champion

class Goblin2(champion):
    name = "goblin2"
    def __init__(self, health = 15, power = 4):
        self.health = health
        self.power = power
        self.winphrase = "The globin kicked you ass and now is raiding your village, you suck."