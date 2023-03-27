import pygad
import numpy as np 

items = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])
capacity = 20
gene_space = [0, 1]
num_genes=100



def fitness_function(solution, solution_idx):
    num_bins = 0
    bins = [0] * int(len(solution) / 10)

    for i in range(0, num_genes, 10):
        item_in_bin = False
        for j in range(len(bins)):
            if solution[i:i+10][j] == 1:
                if bins[j] + items[i//10] <= capacity:
                    bins[j] += items[i//10]
                    item_in_bin = True
                    break
        if not item_in_bin:
            num_bins += 1
            bins.append(items[i//10])

    return num_bins

num_generations = 100
num_parents_mating = 25
sol_per_pop = 50
num_genes = 10
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: ", solution_fitness)
ga_instance.plot_fitness()
