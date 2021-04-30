import gym
import numpy as np

from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO

from environment import EggnoggEnv
from game import Game
import time

game = Game()

env = EggnoggEnv(game, 1, 0)
print(check_env(env))

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=2000)
time.sleep(3)

obs = env.reset()

#for i in range(2000):
#    action, _states = model.predict(obs)
#    obs, rewards, done, info = env.step(action)  
#    env.render()