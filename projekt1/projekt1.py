import pygad
import numpy as np 
import time

# items = np.array([1,2,3,4,5])
# items = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])
items = np.array([2,28,4,26,6,24,8,22,10,20,12,18,14,16,15,15,14,16,12,18,10,20,8,22,6,24,4,26,2,28])
items = items.reshape(-1, 1)
# capacity = 10
# capacity = 20
capacity = 30
# gene_space = [1,2,3,4,5]
# gene_space = [1,2,3,4,5,6,7,8,9,10]
gene_space = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
num_genes=items.size
num_generations = 5000
num_parents_mating = 200
sol_per_pop = 400
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
            return -100
    
    return num_bins*-1

start=time.time()
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       mutation_percent_genes=mutation_percent_genes,
                       gene_space=gene_space,
                       
)

ga_instance.run()
end=time.time()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
if solution_fitness == -1000:
    print("Brak rozwiązania")
else:
    print("Najlepsze rozwiązanie: ", solution_fitness*-1)
print("Najlepsze rozwiązanie: ", solution)
print("Czas: ", end-start)
ga_instance.plot_fitness()
