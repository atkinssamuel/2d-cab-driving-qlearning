from os import system
from time import sleep

import numpy as np


def print_frames(frames):
    for i, frame in enumerate(frames):
        system('cls')
        print(frame['frame'])
        print(f"Time-step: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


def evaluate_agent(env, q_table):
    total_epochs, total_penalties = 0, 0
    episodes = 100

    for _ in range(episodes):
        state = env.reset()
        epochs, penalties, reward = 0, 0, 0

        done = False

        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, info = env.step(action)

            if reward == -10:
                penalties += 1

            epochs += 1

        total_penalties += penalties
        total_epochs += epochs

    print(f"Results after {episodes} episodes:")
    print(f"Average time-steps per episode: {total_epochs / episodes}")
    print(f"Average penalties per episode: {total_penalties / episodes}")


def run_agent(env, q_table, state):
    done = False
    frames = []
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        frame = {
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
        }

        system('cls')
        print(frame['frame'])
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


    print_frames(frames)
