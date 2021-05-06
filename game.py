import numpy as np
import numpy as np
import cv2
import screenshot as sc
import time
import subprocess

p1 = ["w", "a", "s", "d", "v", "b"]
p2 = ["i", "j", "k", "l", "n", "u"]

class Game:
    def __init__(self):
        room = 0;
        self.f = open("./hello.buffer", "a")
        self.frame = sc.screenshot()

    def action(self, keys, player, id):
        keys = np.asarray(keys)
        if player==1:
            self.inputP1(keys,id)
        else:
            self.inputP2(keys,id)

    def reward(self, player):
        frame=self.frame

        # next time work here
        winner = 0
    
        if np.array_equal(frame[100,850],[255,255,25]):
            winner = 1

        if np.array_equal(frame[100,100],[255,25,255]):
            winner = 2
        if player==winner:
            return 1
        elif winner==0:
            return 0
        else:
            return -1


    def renderKey(self,state, key):
        subprocess.call(["xdotool", state, key])

        #self.f.write(string+"\n")
        
    def obs(self):
        self.frame = sc.screenshot()
        return self.frame

    def inputP1(self, keys, id):
        for k in range(len(keys)):
            if(keys[k] == 1):
                self.renderKey("keydown", p1[k])
            else:
                self.renderKey("keyup", p1[k])

    def inputP2(self, keys, id):
        for k in range(len(keys)):
            if(keys[k] == 1):
                self.renderKey("keydown", p2[k])
            else:
                self.renderKey("keyup", p2[k])

    def reset(self, id):
        for k in p1:
            self.renderKey("keyup", k)
        for k in p2:
            self.renderKey("keyup", k)
        self.renderKey("keydown", "F5")
        self.renderKey("keyup", "F5")
        time.sleep(3.5)
    