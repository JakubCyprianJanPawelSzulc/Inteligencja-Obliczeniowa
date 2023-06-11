import gymnasium as gym

# Action Space: Discrete
# Observation Space: Discrete

env = gym.make("CliffWalking-v0", render_mode="human")
env.reset(seed=278784)

moveset = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

for x in moveset:
    action = x
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
env.close()
