#create class

cujo = Pet("Cujo", 50, 20, 20, 1)
cujo.eat_food()
print(cujo.fullness)
print(cujo.happiness)

apollo = Pet("Apollo")
apollo.get_love()
print(apollo.fullness)
print(apollo.happiness)

boomer = Pet("Boomer", 50, 20, 20, 1)
boomer.get_love()
print(boomer.fullness)
print(boomer.happiness)



print(apollo.fulness, apollo.happiness)
apollo.be_alive()
print(apollo.fulness, apollo.happiness)

from oop_16 import Pet
