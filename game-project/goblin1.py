from Champion import champion



class Goblin1(champion):
    name = "goblin1"
    def __init__(self, health = 10, power = 2):
        self.health = health
        self.power = power
        self.winphrase = "The globin kicked you ass and now is raiding your village, you suck."