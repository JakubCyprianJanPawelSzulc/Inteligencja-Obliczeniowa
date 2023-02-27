import pygad
import numpy
import time
from csv import writer
from csv import reader

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

num_parents_mating = 4
num_generations = 10
keep_parents = 2

parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 13
stop_criteria = "reach_1600"

start=time.time()
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
                            mutation_percent_genes=mutation_percent_genes,
                            stop_criteria=stop_criteria)

ga_instance.run()
end=time.time()
print('der Zeit: ',end-start)
with open('zeit.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow([end-start])
    f_object.close()


with open('zeit.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    sumTime = 0
    for row in list_of_rows:
        sumTime += float(row[0])
    print('średni czas dla',len(list_of_rows), 'prób: ',sumTime/len(list_of_rows))
    read_obj.close()


best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
print("Najlepszy wybór: ", best_solution)
print("Wartość przedmiotów w plecaku: ", best_solution_fitness)
print("Nazwy przedmiotów w plecaku:")
names = []
for idx, item in enumerate(items):
    if best_solution[idx] == 1:
        names.append(item['przedmiot'])
print(names)
print("Waga przedmiotów w plecaku: ", sum([item['waga'] for idx, item in enumerate(items) if best_solution[idx] == 1]))
print("Liczba pokoleń: ", ga_instance.generations_completed)
ga_instance.plot_fitness()
