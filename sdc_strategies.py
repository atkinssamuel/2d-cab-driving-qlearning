import random
import numpy as np

from sdc_helpers import *


def unlearned_walk(env, print_flag=True):
    env.s = 328
    epochs = 0
    penalties, reward = 0, 0
    frames = []
    done = False
    while not done:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
        })

        epochs += 1
    print("Timesteps taken: {}".format(epochs))
    print("Penalties incurred: {}".format(penalties))

    if print_flag: print_frames(frames)

    return


def q_learning(env):
    # the rows in the q_table represent the possible states
    # the columns in the q_table represent the possible actions that the agent can take at each state
    q_table = np.zeros([env.observation_space.n, env.action_space.n])

    # Hyperparameters
    alpha = 0.1
    gamma = 0.6
    epsilon = 0.1

    # for plotting
    all_epochs = []
    all_penalties = []

    for i in range(1, 100001):
        state = env.reset()

        epochs, penalties, reward = 0, 0, 0
        done = False

        while not done:
            # if a random number drawn from 0 -> 1 is less than epsilon (0.1), then execute a random action
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            # otherwise, execute the best action given our knowledge
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done, info = env.step(action)

            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -10:
                penalties += 1

            state = next_state
            epochs += 1

        if i % 100 == 0:
            system('cls')
            print(f"Episode: {i}")

    print("Training finished.\n")

    with open("saved_q_tables/q_learning_table.npy", "wb") as q_learning_result_file:
        np.save(q_learning_result_file, q_table)
