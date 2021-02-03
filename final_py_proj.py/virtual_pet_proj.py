# define dict. that holds pets' attributes

puppy = {
    "name": "Cujo",
    "fullness": 50,
    "happiness": 20,
}

# def functions that increase pet's attribute levels.

def feed_pet(pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet["happiness"] += 10

#decrease pet's attr. levels
def get_hungry_and_mopey(pet):
    pet["fullness"] -= 5
    pet["happiness"] -= 5

#prompt user to interact w pet
while True:
    
    print("""
    %s's stats:
    Fullness: %d
    Happiness: %d
    """ % (puppy["name"], puppy ["fullness"], puppy["happiness"]))
    choice = int(input("""
        1. Feed puppy
        2. Play with puppy
        3. Do nothing
    """))

    if choice == 1:
        feed_pet(puppy)
    elif choice == 2:
        play_with_pet(puppy)
    else:
        pass

        #each time the loop runs, pet will need attention
    get_hungry_and_mopey(puppy)