import gym
import json

from baselines.common.policies import MlpPolicy
from baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

from environment import EggnoggEnv
from game import Game
import time

env = DummyVecEnv([lambda: EggnoggEnv()])

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(20000):
  goal = time.time() + 300
  action, _states = model.predict(obs)
  obs, rewards, done, info = env.step(action)  
  env.render()
  if(time.time() < goal):
    time.sleep(goal-time.time())