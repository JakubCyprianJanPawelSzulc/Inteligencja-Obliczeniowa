import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)


def run_solution(solution):
    reward = 0
    for step in solution:
        observation, reward, terminated, truncated, info = env.step(int(step))
        if terminated or truncated:
            break
    env.reset(seed=42)
    return reward


# Fitness value of the best solution = 120.59311053864306


sol = [2, 1, 2, 1, 2, 0, 0, 1, 1, 1, 3, 0, 1, 1, 3, 1, 0, 2, 1, 0, 0, 0, 0, 0,
       3, 1, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 3, 3, 0, 1, 0, 1, 2, 3, 0, 2, 0, 3,
       2, 2, 0, 0, 3, 3, 3, 0, 0, 2, 3, 2, 0, 3, 1, 2, 0, 1, 3, 1, 3, 2, 2, 0,
       2, 3, 1, 0, 0, 3, 3, 2, 0, 0, 3, 3, 0, 1, 3, 0, 1, 0, 0, 2, 3, 0, 3, 1,
       3, 0, 3, 3]

run_solution(sol)
