import gymnasium as gym
import numpy as np

# Value Iteration Algorithm

def value_iteration(env, gamma=0.9, theta=1e-6):
    V = np.zeros(env.observation_space.n)
    while True:
        delta = 0
        for s in range(env.observation_space.n):
            v = V[s]
            q_values = []
            for a in range(env.action_space.n):
                q_value = 0
                for prob, next_state, reward, done in env.P[s][a]:
                    q_value += prob * (reward + gamma * V[next_state])
                q_values.append(q_value)
            V[s] = max(q_values)
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

env = gym.make('FrozenLake-v1')
optimal_values = value_iteration(env)
helper = []
for i in optimal_values:
    helper.append(round(i * 4))
print(helper)
