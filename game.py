import numpy as np
import numpy as np
import cv2
import screenshot as sc
import time

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
        else:
            return 0


    def toBuffer(self,string):
        string = string[6:]
        print(string)

        #self.f.write(string+"\n")
        
    def obs(self):
        self.frame = sc.screenshot()
        return self.frame

    def inputP1(self, keys, id):
        print(keys)
        for k in range(len(keys)):
            if(keys[k] == 1):
                self.toBuffer(str(id)+" gym d "+p1[k])
            else:
                self.toBuffer(str(id)+" gym u "+p1[k])

    def inputP2(self, keys, id):
        for k in range(len(keys)):
            if(keys[k] == 1):
                self.toBuffer(str(id)+" gym d "+p2[k])
            else:
                self.toBuffer(str(id)+" gym u "+p2[k])

    def reset(self, id):
        self.toBuffer(str(id)+" gym d F5")
        self.toBuffer(str(id)+" gym u F5")
        time.sleep(3.5)
    