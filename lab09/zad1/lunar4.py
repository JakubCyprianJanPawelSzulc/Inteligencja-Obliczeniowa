import gym

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)

print("Stan początkowy: ", observation)

for _ in range(300):
   action = env.action_space.sample()
   observation, reward, terminated, truncated, info = env.step(action)
 
   if terminated or truncated:
      print("Stan końcowy: ", observation)
      observation, info = env.reset()
      print("Reset, nowy stan początkowy: ", observation)
env.close()