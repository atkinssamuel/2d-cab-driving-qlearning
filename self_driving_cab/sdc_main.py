import gym
import sys

# sys.path.append("../self_driving_cab")

from sdc_strategies import *

'''
useful env methods:
env.reset() - resets the environment and returns a random initial state

env.step(action) - step the environment by one time-step. Returns:
    observation: observation of the environment
    reward: if your action was beneficial or not
    done: indicates if we have successfully picked up and dropped off a passenger, (aka an episode)
    info: additional info such as performance and latency for debugging purposes

env.render() - renders one frame of the environment

state env.encode(c1, c2, ..., cn) - returns a state using the specified coordinate values



useful env properties:
env.action_space - total # of possible actions

env.observation_space - total # of possible states

env.state - the state of the environment [0 -> env.action_space]

env.P[state_encoding] - returns the reward table associated with a given state
                        list({action: [(probability, nextstate, reward, done)]}, ...)
'''





if __name__ == "__main__":
    env = gym.make("Taxi-v3").env
    frames = unlearned_walk(env)
    print_frames(frames)
