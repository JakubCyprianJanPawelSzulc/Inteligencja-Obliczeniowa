import gymnasium as gym

# Action Space: Discrete
# Observation Space: Discrete

env = gym.make("FrozenLake-v1", render_mode="human")
env.reset(seed=2137)

moveset = [2, 2, 1, 1, 1, 2, 1]

for x in moveset:
    action = x
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
env.close()
