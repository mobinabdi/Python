import random
import matplotlib.pyplot as plt

%matplotlib inline

random.seed()

people = []
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 10000):
    for person1 in range(0, 50):
        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)
        if people[person1] != 0:
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1
#sort
#people.sort()
plt.bar(range(0, 50), sorted(people,reverse=Ture))
plt.show()