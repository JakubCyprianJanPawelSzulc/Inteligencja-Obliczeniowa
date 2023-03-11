import time
import numpy as np
import pygad
import math

plansza = [[0,0,0,0,0,0,0,0,0,0,0,0],
           [0,2,1,1,0,1,1,1,0,1,1,0],
           [0,0,0,1,1,1,0,1,0,0,1,0],
           [0,1,1,1,0,1,0,1,1,1,1,0],
           [0,1,0,1,0,0,1,1,0,0,1,0],
           [0,1,1,0,0,1,1,1,0,1,1,0],
           [0,1,1,1,1,1,0,1,1,1,0,0],
           [0,1,0,1,1,0,0,1,0,1,1,0],
           [0,1,0,0,0,1,1,1,0,0,1,0],
           [0,1,0,1,0,0,1,0,1,0,1,0],
           [0,1,0,1,1,1,1,1,1,1,3,0],
           [0,0,0,0,0,0,0,0,0,0,0,0]]

gene_space = [0,1,2,3,4]

# 1-góra
# 2-dół
# 3-lewo
# 4-prawo

num_genes = 30

parent_selection_number = 10
number_generations = 10000
keep_parents = 4
parent_selection_type = "sss"
mutation_percent_genes = 8
sol_per_pop = 100

def fitness_func(solution, solution_idx):
    x = 1
    y = 1
    steps = 0
    wallHits = 0
    endCoords=[10,10]
    for gene in solution:
        if gene == 0:
            continue
        if gene == 1:
            if plansza[y-1][x] == 0:
                wallHits += 1
            else:
                y -= 1
                steps += 1
        elif gene == 2:
            if plansza[y+1][x] == 0:
                wallHits += 1
            else:
                y += 1
                steps += 1
        elif gene == 3:
            if plansza[y][x-1] == 0:
                wallHits += 1
            else:
                x -= 1
                steps += 1
        elif gene == 4:
            if plansza[y][x+1] == 0:
                wallHits += 1
            else:
                x += 1
                steps += 1
        if steps >= 30:
            break

    final_x_distance = abs(x - endCoords[0])
    final_y_distance = abs(y - endCoords[1])
    final_distance_to_end = final_x_distance + final_y_distance
    fitness = 1000/(steps + 1 + wallHits + final_distance_to_end*50)

    return fitness
    
fitness_function = fitness_func

ga_instance = pygad.GA(gene_space=gene_space,
                          num_generations=number_generations,
                            num_parents_mating=parent_selection_number,
                            fitness_func=fitness_function,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            parent_selection_type=parent_selection_type,
                            keep_parents=keep_parents,
                            mutation_percent_genes=mutation_percent_genes)



ga_instance.run()
best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie:")
print(best_solution)
print("Fitness najlepszego rozwiązania:")
print(best_solution_fitness)
ga_instance.plot_fitness()
