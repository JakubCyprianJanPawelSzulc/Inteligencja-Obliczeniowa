import gymnasium as gym
import numpy
import pygad
from bestSolution2 import run_solution

env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False)


observation, info = env.reset(seed=2137)


def run_solution(solution):
    reward = 0
    for step in solution:
        observation, reward, terminated, truncated, info = env.step(int(step))
        if terminated or truncated:
            break
    env.reset(seed=2137)
    return reward

def fitness_func(ga_instance, solution, solution_idx):
    return run_solution(solution)

# solution jest przekazywane do funkcji run_solution
# symuluje rozgrywkę wykonując akcje zgodnie z wartościami w wektorze solution
# funkcja run_solution zwraca nagrodę uzyskaną w trakcie rozgrywki.


fitness_function = fitness_func

num_generations = 50
num_parents_mating = 10

sol_per_pop = 60
num_genes = 64

parent_selection_type = "sss"
keep_parents = 10

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
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
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

env.close()
