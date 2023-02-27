import pygad
import numpy

items = [{'przedmiot': 'zegar', 'wartosc': 100, 'waga': 7},
        {'przedmiot': 'obraz-pejzaz', 'wartosc': 300, 'waga': 7},
        {'przedmiot': 'obraz-portret', 'wartosc': 200, 'waga': 6},
        {'przedmiot': 'radio', 'wartosc': 40, 'waga': 2},
        {'przedmiot': 'laptop', 'wartosc': 500, 'waga': 5},
        {'przedmiot': 'lampka nocna', 'wartosc': 70, 'waga': 6},
        {'przedmiot': 'srebrne sztućce', 'wartosc': 100, 'waga': 1},
        {'przedmiot': 'porcelana', 'wartosc': 250, 'waga': 3},
        {'przedmiot': 'figura z brązu', 'wartosc': 300, 'waga': 10},
        {'przedmiot': 'skórzana torebka', 'wartosc': 280, 'waga': 3},
        {'przedmiot': 'odkurzacz', 'wartosc': 300, 'waga': 15}]

def fitness_func(solution, solution_idx):
    value_sum = 0
    weight_sum = 0
    for idx, item in enumerate(items):
        if solution[idx] == 1:
            value_sum += item['wartosc']
            weight_sum += item['waga']
    if weight_sum > 25:
        fitness = 0
    else:
        fitness = value_sum
    return fitness

fitness_function = fitness_func

gene_space = [0, 1]
sol_per_pop = 50
num_genes = len(items)

num_parents_mating = 5
num_generations = 20
keep_parents = 2

parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 8

ga_instance = pygad.GA(gene_space=gene_space,
                          num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            fitness_func=fitness_function,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            parent_selection_type=parent_selection_type,
                            keep_parents=keep_parents,
                            crossover_type=crossover_type,
                            mutation_type=mutation_type,
                            mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
print("Najlepszy wybór: ", best_solution)
print("Wartość przedmiotów w plecaku: ", best_solution_fitness)
print("Nazwy przedmiotów w plecaku:")
for idx, item in enumerate(items):
    if best_solution[idx] == 1:
        print(item['przedmiot'])
print("Waga przedmiotów w plecaku: ", sum([item['waga'] for idx, item in enumerate(items) if best_solution[idx] == 1]))
ga_instance.plot_result()
