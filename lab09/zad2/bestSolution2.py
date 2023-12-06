import gymnasium as gym

env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False, render_mode="human")
observation, info = env.reset(seed=2137)


def run_solution(solution):
    reward = 0
    for step in solution:
        observation, reward, terminated, truncated, info = env.step(int(step))
        if terminated or truncated:
            break
    env.reset(seed=2137)
    return reward


sol = [0, 0, 0, 0, 0, 3, 3, 2, 2, 1, 3, 1, 2, 2, 3, 3, 1, 2, 3, 1, 2, 2, 2, 2,
       0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 0, 0, 1, 2, 1, 3, 1, 0, 0, 0, 1,
       0, 2, 1, 1, 2, 2, 3, 2, 3, 1, 3, 1, 3, 0, 2, 1]

run_solution(sol)