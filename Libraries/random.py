import random 

# returns random default number
def generate_random():
    return random.random()

# returns a random element of a given iterable
def pick_random(l: list):
    return random.choice(l)
