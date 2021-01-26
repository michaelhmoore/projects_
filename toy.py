class Toy:
    def __init__(self, bonus=10, newness=10)
        self.bonus = 10
        self.newness = 10

    def use(self):
        if self.newness == 0:
            return 0
        else:
            self.newness -= 1
            return self.bonus

    