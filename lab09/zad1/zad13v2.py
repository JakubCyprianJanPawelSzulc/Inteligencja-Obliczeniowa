import gymnasium as gym

# Action Space: Discrete
# Observation Space: Discrete

env = gym.make("FrozenLake-v1", render_mode="human")
env.reset(seed=278784)

moveset = [2, 2, 2, 1, 1, 2, 2]

for x in moveset:
    action = x
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
env.close()
