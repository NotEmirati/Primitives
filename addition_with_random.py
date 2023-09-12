import random

def addition(firstInput:int, secondInput:int):
    randomInput = random.randint(0,100)
    total = firstInput + secondInput + randomInput
    if total > 100:
        print('Total exceeds 100')
    else:
        print('The task is complete. The result is:')
        print(total)
    return total

addition(20,10)
