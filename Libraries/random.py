import random 

# returns random default number
def generate_random():
    return random.random()

# returns a random element of a given iterable
def pick_random(l: list):
    return random.choice(l)

# returns a random int from range
def generate_random_int(start: int, finish: int):
    return random.randint(start, finish)

# shuffles the given list
def shuffle_iterable(l:list):
    random.shuffle(l)
    return l

# return random float from given range
def random_float(start: float, finish: float):
    return random.uniform(start, finish)
