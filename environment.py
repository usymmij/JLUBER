import gym
from gym import spaces
# https://github.com/mherkazandjian/fastgrab
# use fastgrab to get screenshots

class EggnoggEnv(gym.Env):
    """Eggnogg enviornment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, screen):
        super(EggnoggEnv, self).__init__()
        self.screen = screen
        self.reward_range = (-2, 2)
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(6)
        # Example for using image as input:
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(540, 960, 3)
            , dtype=np.uint8)

    def step(self, action):
        self._take_action(action)

        # Execute one time step within the environment
    def reset(self):
        self.score = 0
        self.rooms_won = 0
        self.rooms_lost = 0
        self.kills = 0
        self.deaths = 0
        # Reset the state of the environment to an initial state
    
        self.current_step = 0

    def render(self, mode='human', close=False):
        print("score: "+str(self.score))
        print("rooms won: "+self.rooms_won)
        print("rooms lost: "+self.rooms_lost)
        print("kills: "+self.kills)
        print("deaths: "+self.deaths)
        print("step: "+self.current_step)