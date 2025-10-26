import random

def randomizer(questions): #slumpar fram den ordning som frågorna ska komma i
    x = [i for i in range(len(questions))]
    random.shuffle(x)
    return x
