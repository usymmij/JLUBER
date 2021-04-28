import gym
import numpy as np

from baselines.common.vec_env import DummyVecEnv

from environment import EggnoggEnv
from game import Game
import time

game = Game()
env = DummyVecEnv([lambda: EggnoggEnv(game, 1, 0)])
time.sleep(3)
obs = env.reset()
action = [1,0,0,1,0,0]
for i in range(2000):
    obs, rewards, done, info = env.step(action)
    env.render()