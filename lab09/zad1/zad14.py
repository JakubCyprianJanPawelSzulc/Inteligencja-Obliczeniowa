import gymnasium as gym

# Action Space: Continuous
# Observation Space: Continuous

env = gym.make("Ant-v4", render_mode="human")
env.reset()

while True:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    if truncated:
        break
env.close()
