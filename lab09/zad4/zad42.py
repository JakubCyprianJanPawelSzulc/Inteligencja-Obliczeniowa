import gymnasium as gym
import numpy as np

environment = gym.make("FrozenLake-v1", is_slippery=False)
environment.reset()
environment.render()

qtable = np.zeros((environment.observation_space.n, environment.action_space.n))

episodes = 1000
alpha = 0.5
gamma = 0.9

outcomes = []

for _ in range(episodes):
    state = environment.reset()
    done = False

    outcomes.append("Failure")

    while not done:

        if np.max(qtable[state]) > 0:
            action = np.argmax(qtable[state])


        else:
            action = environment.action_space.sample()

        new_state, reward, done, info = environment.step(action)

        qtable[state, action] = qtable[state, action] + alpha * (
                reward + gamma * np.max(qtable[new_state]) - qtable[state, action])

        state = new_state

        if reward:
            outcomes[-1] = "Success"

episodes = 100
nb_success = 0

for _ in range(100):
    state = environment.reset()
    done = False

    while not done:

        if np.max(qtable[state]) > 0:
            action = np.argmax(qtable[state])

        else:
            action = environment.action_space.sample()

        new_state, reward, done, info = environment.step(action)

        state = new_state

        nb_success += reward

from IPython.display import clear_output
import time

state = environment.reset()
done = False
sequence = []

while not done:

    if np.max(qtable[state]) > 0:
        action = np.argmax(qtable[state])


    else:
        action = environment.action_space.sample()

    sequence.append(action)

    new_state, reward, done, info = environment.step(action)

    state = new_state

    clear_output(wait=True)
    environment.render()
    time.sleep(1)

print(sequence)
