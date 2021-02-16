from os import system
from time import sleep


def print_frames(frames):
    for i, frame in enumerate(frames):
        system('cls')
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)