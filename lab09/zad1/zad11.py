import gymnasium as gym

# Action Space: Discrete
# Observation Space: Continuous

env = gym.make("MountainCar-v0", render_mode="human")
observation, _ = env.reset()

while True:
    position, velocity = observation
    if velocity < 0:
        action = 0
    elif velocity >= 0:
        action = 2
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
env.close()
