import gymnasium as gym

# Action Space: Discrete/Continuous
# Observation Space: Image

env = gym.make("CarRacing-v2", render_mode="human")
env.reset()

for _ in range(4000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
env.close()
