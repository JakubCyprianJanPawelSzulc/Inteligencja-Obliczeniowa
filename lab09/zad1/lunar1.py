import gym

env = gym.make("LunarLander-v2", render_mode="human")
env.reset(seed=2)

for _ in range(300):
   action = 1 #odpal lewy silnik
   env.step(action)
env.close()