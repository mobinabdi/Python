import random

random.seed()

cont = [0,0,0,0,0,0];

tas = random.randint(1,6)

cont[tas - 1] = cont[tas - 1] + 1
print(cont)
