import gym
from gym import spaces
from game import Game
import time
import numpy as np

class EggnoggEnv(gym.Env):
    """Eggnogg enviornment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, gameEnv, player, instance):
        # gameEnv: the game object eggnogg runs in
        # player: player 1: blue, left; 2: pink, right
        # instance: the game instance

        super(EggnoggEnv, self).__init__()
        self.current_step = 0
        self.env = gameEnv
        self.p = player
        self.instance = instance
        self.reward_range = (-1, 1)
        self.score = 0
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.MultiBinary(6)
        # Example for using image as input:
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(640, 950, 3)
            , dtype=np.uint8)
        self.obs = np.zeros((960,640,3))

        self.time_start = time.time()
            
    def step(self, action):
        self.env.action(action, self.p, self.instance)

        self.current_step += 1
        self.obs = self.env.obs()

        reward = self.env.reward(self.p)
        self.score = reward
        done = time.time() - self.time_start > 60
        

        return self.obs, reward, done, {}

        # Execute one time step within the environment
    def reset(self):
        self.env.reset(self.instance)
        print("score: "+str(self.score))
        print("step: "+str(self.current_step))
        self.score = 0
        self.time_start = time.time()
        self.current_step = 0
        self.obs=self.env.obs()
        return self.obs
        # Reset the state of the enviro1619058245.2927094

    def render(self, mode='humwdban', close=False):
        print("score: "+str(self.score))
        #cv2.imshow("window", self.obs)