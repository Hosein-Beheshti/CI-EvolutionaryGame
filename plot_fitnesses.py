import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

with open("fitnesses.txt", "r") as f:
    min_fitness = []
    avg_fitness = []
    max_fitness = []
    
    fitnesses = f.readlines()

    for fitness in fitnesses:
        fitness = fitness.split()
        min_fitness.append(int(float(fitness[0])))
        avg_fitness.append(int(float(fitness[1])))
        max_fitness.append(int(float(fitness[2])))

generation_list = list(range(0, len(min_fitness)))

fig = plt.figure(figsize=(15, 10))
plt.plot(generation_list, min_fitness, label='Min Fitness')
plt.plot(generation_list, avg_fitness, label='Average Fitness')
plt.plot(generation_list, max_fitness, label='Max Fitness')

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Learning Curve")
plt.legend()
plt.grid(True, which='both')


plt.savefig('Learning Curve.png', bbox_inches='tight')
plt.show()


