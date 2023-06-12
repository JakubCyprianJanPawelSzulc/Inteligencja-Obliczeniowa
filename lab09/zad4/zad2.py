import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

#Deep Q-Network (DQN)

def build_dqn(input_dim, output_dim):
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(output_dim, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())
    return model

def dqn(env, num_episodes=1000, gamma=0.9, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995):
    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.n
    model = build_dqn(num_states, num_actions)

    for episode in range(num_episodes):
        state = env.reset()
        state = np.reshape(state, [1, num_states])
        done = False

        while not done:
            if np.random.rand() <= epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(model.predict(state)[0])

            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, num_states])

            target = reward + gamma * np.amax(model.predict(next_state)[0])
            target_vec = model.predict(state)[0]
            target_vec[action] = target

            model.fit(state, target_vec.reshape(-1, num_actions), epochs=1, verbose=0)

            state = next_state

        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

    policy = np.argmax(model.predict(np.identity(num_states)), axis=1)
    return model, policy


env = gym.make("FrozenLake-v1", is_slippery=False)
model, policy = dqn(env)

print("Optimal policy:")
print(policy)
