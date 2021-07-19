from numpy.core.defchararray import array
from numpy.core.fromnumeric import argmax
from numpy.lib.function_base import select
from player import Player
import numpy as np
from config import CONFIG
from copy import deepcopy
from random import choices, randint


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        weights = child.nn.weights
        biases = child.nn.biases

        probability = 0.2
        mu, sigma = 0, 0.2
        for i in range(len(weights)):
            normal = np.random.normal(mu, sigma, size=(weights[i].shape))
            nums = np.random.choice([0,1], size=(weights[i].shape), p=[1-probability, probability])
            rand_normal = nums * normal
            weights[i] = weights[i] + rand_normal

        for i in range(len(biases)):
            normal = np.random.normal(mu, sigma, size=(biases[i].shape))
            nums = np.random.choice([0,1], size=(biases[i].shape), p=[1-probability, probability])
            rand_normal = nums * normal
            biases[i] = biases[i] + rand_normal
        
        
        # child: an object of class `Player`



    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # prev_players.sort(key=lambda x: x.fitness, reverse=True)
            prev_playersـcopy = deepcopy(prev_players)
            # new_players = new_players[: num_players]


            # TODO (additional): a selection method other than `fitness proportionate`
            # ROULETTE WHEEL
            fitnesses = np.zeros(len(prev_playersـcopy))
            for i in range(len(fitnesses)):
                fitnesses[i] = prev_playersـcopy[i].fitness

            new_players = []
            selected_players = np.random.choice(prev_playersـcopy, size=num_players, p=fitnesses/sum(fitnesses), replace=True)
            for i in range(num_players):
                new_players.append(deepcopy(selected_players[i]))

            # TOURNOMENT
            # new_players = []
            # q = 5
            # for i in range(num_players):
            #     rand_players = np.random.choice(prev_playersـcopy, q)
            #     fitnesses = np.zeros(q)
            #     for i in range(q):
            #         fitnesses[i] = rand_players[i].fitness
            #     index = argmax(fitnesses)
            #     new_players.append(deepcopy(rand_players[index]))


            #     new_players.append(deepcopy(prev_playersـcopy[index]))
            #     prev_playersـcopy.pop(index)
            #     fitnesses.pop(index)




            # TODO (additional): implementing crossover
            # new_players = []
            # for child in range(num_players):
            #     parents = choices(prev_players, k=2)
            #     child = deepcopy(parents[0])
            #     child.nn.weights[1][10:14] = deepcopy(parents[1].nn.weights[1][10:14])
            #     child.nn.biases[1][5:10] = deepcopy(parents[1].nn.biases[1][5:10])
            #     # child.weights[1][5:10] = deepcopy(parents[1].weights[1][5:10])
            #     # print(child.weights[1][5:10])

            #     new_players.append(child)


            for player in new_players:
                self.mutate(player)


            return new_players

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        players.sort(key=lambda x: x.fitness, reverse=True)

        # print(np.where(players(key=lambda x: x.fitness) == y))
    
        # best_players = players[: num_players]
        # print(len(best_players))
        # TODO (additional): a selection method other than `top-k`
        # ROULETTE WHEEL
        # prev_playersـcopy = deepcopy(players)
        # fitnesses = np.zeros(len(prev_playersـcopy))
        # for i in range(len(fitnesses)):
        #     fitnesses[i] = prev_playersـcopy[i].fitness

        # new_players = []
        # selected_players = np.random.choice(prev_playersـcopy, size=num_players, p=fitnesses/sum(fitnesses), replace=False)
        # for i in range(num_players):
        #     new_players.append(deepcopy(selected_players[i]))
            
        # # TODO (additional): plotting
        fitnesses = np.zeros(len(players))
        for i in range(len(fitnesses)):
            fitnesses[i] = players[i].fitness

        min_fitness = fitnesses.min()
        max_fitness = fitnesses.max()
        average_fitness = np.average(fitnesses)

        # write to file
        with open('fitnesses.txt', 'a') as filehandle:
            filehandle.write(f"{min_fitness} {average_fitness} {max_fitness}")
            filehandle.write("\n")


        return players[: num_players]
