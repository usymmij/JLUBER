import gym
import numpy as np

from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO

from environment import EggnoggEnv
from game import Game
import time

time.sleep(1)
game = Game()

env = EggnoggEnv(game, 1, 0)
print(check_env(env))

model = PPO.load("ppo_eggnogg.zip", env, verbose=1)

obs = env.reset()

for i in range(2000):
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)  
    if reward != 0:
        env.reset()