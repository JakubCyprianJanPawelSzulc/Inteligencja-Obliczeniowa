import pygad
import numpy as np 

weights = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])



def fitness(solution, solution_idx):
    num_bins = len(solution) // capacity
    bins = [0] * num_bins

    for i in range(len(solution)):
        bin_index = i % num_bins
        if solution[i] == 1:
            if bins[bin_index] + items[i] <= capacity:
                bins[bin_index] += items[i]
            else:
                num_bins += 1
                bins.append(items[i])

    return num_bins

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