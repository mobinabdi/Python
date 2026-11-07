import random

random.seed()

cont = [0,0,0,0,0,0]

for i in range(0,10000):
    tas = random.randint(1,6)
    cont[tas - 1] = cont[tas - 1] + 1

print(cont)
