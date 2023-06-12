import gym

# Action Space: Discrete
# Observation Space: Image

env = gym.make("ALE/SpaceInvaders-v5", render_mode="human")
env.reset()

for _ in range(100):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        env.close()
        break
env.close()
