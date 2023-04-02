import pygad
import numpy as np 
import time
from csv import writer
import random


# items1 = np.array([1,2,3,4,5])
# items2 = np.array([1,1,1,5,5])
# items3 = np.array([2,8,1,6,3])


# items1 = np.array([1,9,2,8,3,7,4,6,5,5,4,6])
# items2 = np.array([10,10,10,10,10,1,1,1,1,1,2,2])
# items3 = np.array([8,2,9,1,7,3,6,4,5,5,4,6])

items1 = np.array([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,10,10,5,4,1])
items2 = np.array([10,10,10,10,10,10,10,10,10,10,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,10,10,5,4,1])
items3 = np.array([8,2,9,1,7,3,6,4,5,5,4,6,8,2,9,1,7,3,6,4,5,5,4,6,8,2,9,1,7,3])

capacity = 10

# gene_space = [1,2,3,4,5]
# gene_space = [1,2,3,4,5,6,7,8,9,10,11,12]
gene_space = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

num_genes=items1.size
num_generations = 20000
num_parents_mating = 100
sol_per_pop = 300
mutation_percent_genes = 12
keep_parents = 15



def fitness_function(solution, solution_idx):
    bins=np.unique(solution)
    num_bins = bins.size

    for i in range(num_bins):
        bin_sum = 0
        for j in range(len(solution)):
            if solution[j] == bins[i]:
                bin_sum += random_items[j]
        if bin_sum > capacity:
            return -100
    
    return num_bins*-1


for i in range(100):
    random_items = random.choice([items1, items2, items3])
    random_items = random_items.reshape(-1, 1)

    start=time.time()
    ga_instance = pygad.GA(num_generations=num_generations,
                        num_parents_mating=num_parents_mating, 
                        fitness_func=fitness_function,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        mutation_percent_genes=mutation_percent_genes,
                        gene_space=gene_space,
                        parent_selection_type="sss",
                        keep_parents=keep_parents,
                        
    )

    ga_instance.run()
    end=time.time()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    if solution_fitness*-1 <= 15:
        with open('zeit3.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([end-start, solution_fitness*-1])
            f_object.close()
        print("Najlepsze rozwiązanie: ", solution_fitness*-1)
    else:
        with open('zeit3.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([0, solution_fitness*-1])
            f_object.close()
        # print("Najlepsze rozwiązanie: ", solution)
        # print("Czas: ", end-start)
    # ga_instance.plot_fitness()
