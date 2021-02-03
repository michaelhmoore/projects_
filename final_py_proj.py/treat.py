class Treat:
    def __init__(self, yum=10, joy=10):
        self.yum = yum
        self.joy = joy


class ColdPizza(Treat):
    def __init__(self):
        super().__init__(15, 20)

class Bacon(Treat):
    def __init__(self):
        super().__init__(30, 30)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__(2, 1)
