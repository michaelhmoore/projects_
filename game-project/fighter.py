class champion:
    name = "champion"

    def is_alive(self):
        """
        #see's if hero is alive
        """
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):

        enemy.health -= self.power
        if not enemy.is_alive():
            enemy.health = 0
        print("%s does %d damage to %s." % (self.name,self.power,enemy.name))
        
        if not enemy.is_alive():
            print(self.winphrase)
    
    def print_status(self):
        print("%s has %d health and %d power."% (self.name, self.health, self.power))
    
    def level_up(self):
        self.health = self.health * 3
        self.power = self.power * 5