import random
import pygad

bin_capacity = 10
item_sizes = [random.randint(1, 10) for i in range(10)]
num_items = len(item_sizes)

def fitness_func(solution, solution_idx):
    bin_sizes = [0] * len(solution)
    for item_idx in range(num_items):
        bin_idx = solution[item_idx]
        bin_sizes[bin_idx] += item_sizes[item_idx]
    num_bins = 0
    for bin_size in bin_sizes:
        if bin_size > 0:
            num_bins += 1
    fitness = 1.0 / num_bins
    return fitness


num_generations = 50
num_parents_mating = 4
mutation_rate = 0.05
population_size = 10

ga_instance = pygad.GA(
    num_generations=num_generations, 
    num_parents_mating=num_parents_mating, 
    mutation_percent_genes=mutation_rate*100, 
    initial_population=None, 
    fitness_func=fitness_func,
    num_solutions=population_size, 
    num_genes=num_items, 
    gene_space=list(range(population_size)),
)


solution, fitness = ga_instance.best_solution()
print("Najlepsze rozwiązanie: ", solution)
