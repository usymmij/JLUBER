import gym
import json

from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO

from environment import EggnoggEnv
from game import Game
import time

game = Game()

env = EggnoggEnv(game, 1, 0)
print(check_env(env))

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(20000):
  goal = time.time() + 300
  action, _states = model.predict(obs)
  obs, rewards, done, info = env.step(action)  
  env.render()
  if(time.time() < goal):
    time.sleep(goal-time.time())