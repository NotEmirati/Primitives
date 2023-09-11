import random

def addition(firstInput:int, secondInput:int):
    randomInput = random.randint(0,100)
    total = firstInput + secondInput + randomInput
    return total

total = 0

print(addition(5,6))
