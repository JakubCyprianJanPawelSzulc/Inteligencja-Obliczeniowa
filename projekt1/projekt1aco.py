import numpy as np
import aco

items = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 10])
capacity = 20

n_ants = 10
n_iterations = 100
evaporation_rate = 0.5
alpha = 1
beta = 2
Q = 1
initial_pheromone = 0.1

num_bins = len(items)
pheromone_matrix = np.ones((num_bins, capacity)) * initial_pheromone

def fitness_function(solution):
    bins=np.unique(solution)
    num_bins = bins.size

    for i in range(num_bins):
        bin_sum = 0
        for j in range(len(solution)):
            if solution[j] == bins[i]:
                bin_sum += items[j]
        if bin_sum > capacity:
            return -1
    
    return num_bins*-1

def transition_rule(state, pheromone_matrix, alpha, beta):
    probabilities = np.zeros(pheromone_matrix.shape)
    probabilities[state == -1] = 1.0
    probabilities[state != -1] = pheromone_matrix[state != -1]**alpha * ((1.0/fitness_function(state[state!=-1]))**beta)
    probabilities = probabilities / np.sum(probabilities)
    return probabilities

def update_rule(pheromone_matrix, solutions, Q):
    delta_pheromone = np.zeros(pheromone_matrix.shape)
    for i in range(len(solutions)):
        for j in range(len(solutions[i])):
            if solutions[i][j] != -1:
                delta_pheromone[solutions[i][j], j] += Q / fitness_function(solutions[i])
    pheromone_matrix = (1.0 - evaporation_rate) * pheromone_matrix + delta_pheromone
    return pheromone_matrix

aco_obj = aco.AntColony(ant_count=n_ants, iterations=n_iterations, rule=transition_rule,
                        update_rule=update_rule, fitness_function=fitness_function,
                        pheromone_matrix=pheromone_matrix, alpha=alpha, beta=beta, Q=Q)
aco_obj.run()

best_solution = aco_obj.best_solution()
print("Best solution:", best_solution)
print("Fitness value:", fitness_function(best_solution))
