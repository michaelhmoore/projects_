from Champion import champion


class Dragon(champion):
    name = "dragon"
    def __init__(self, health = 150, power = 20):
        self.health = health
        self.power = power
        self.winphrase = "The dragon lets a breath of fire out and burns you to a crisp and you die... Game over."