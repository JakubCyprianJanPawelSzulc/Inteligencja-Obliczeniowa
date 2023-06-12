import pygad
import numpy as np
import gym

env = gym.make("LunarLander-v2")
obervation, info = env.reset(seed=2137)

def fitness_func(solution, solution_idx):
    for step in solution:
        observation, reward, terminated, truncated, info = env.step(int(step))
        if terminated or truncated:
            break
    env.reset(seed=2137)
    return reward


num_generations = 50
num_parents_mating = 10

sol_per_pop = 60
num_genes = 100

parent_selection_type = "sss"
keep_parents = 10

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_space=[0,1,2,3],
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)


ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: {solution}".format(solution=solution))
print("Wynik fitness dla najlepszego rozwiązania: {solution_fitness}".format(solution_fitness=solution_fitness))