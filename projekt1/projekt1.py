import pygad
import numpy as np 

# items = np.array([1,2,3,4,5])
items = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])
items = items.reshape(-1, 1)
# capacity = 10
capacity = 20
# gene_space = [1,2,3,4,5]
gene_space = [1,2,3,4,5,6,7,8,9,10]
num_genes=items.size
num_generations = 2000
num_parents_mating = 25
sol_per_pop = 50
mutation_percent_genes = 10


def fitness_function(solution, solution_idx):
    bins=np.unique(solution)
    num_bins = bins.size

    for i in range(num_bins):
        bin_sum = 0
        for j in range(len(solution)):
            if solution[j] == bins[i]:
                bin_sum += items[j]
        if bin_sum > capacity:
            return -1000
    
    return num_bins*-1


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       mutation_percent_genes=mutation_percent_genes,
                       gene_space=gene_space,)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
if solution_fitness == -1000:
    print("Brak rozwiązania")
else:
    print("Najlepsze rozwiązanie: ", solution_fitness*-1)
print("Najlepsze rozwiązanie: ", solution)
ga_instance.plot_fitness()
