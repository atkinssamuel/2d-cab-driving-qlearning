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
