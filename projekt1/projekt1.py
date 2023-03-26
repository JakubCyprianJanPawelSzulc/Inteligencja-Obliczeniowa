import pygad
import numpy as np 

weights = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])

def fitness_func(solution, solution_idx):
    capacity = 10
    bins = np.zeros(len(weights))
    bin_idx = 0
    for i in range(len(weights)):
        if bins[bin_idx] + weights[i] <= capacity:
            bins[bin_idx] += weights[i]
        else:
            bin_idx += 1
            bins[bin_idx] += weights[i]
    return -1*(bin_idx+1)

num_generations = 100
num_parents_mating = 25
sol_per_pop = 50
num_genes = 10
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: ", solution)