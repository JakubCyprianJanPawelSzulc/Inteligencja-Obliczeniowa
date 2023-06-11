import gym

env = gym.make("LunarLander-v2", render_mode="human")
env.reset(seed=8)

for _ in range(300):
   action = env.action_space.sample()
   env.step(action)
env.close()