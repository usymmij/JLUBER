import subprocess

states = ["closed", "main", "maps", "game", "esc" ]
# rooms: -4 to 4

# print the output
# print(out.decode("utf-8"))


class EggnoggInterface:
    def __init__(self):
        self.room = 0
        self.state = states[0]
        self.proc = subprocess.Popen(['cat'],
            stdin =subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=0)
        
        self.bash("andljnsadklna \n echo sajndla")
        self.bash('save="DISPLAY"')
        self.bash("export DISPLAY=:44 ")
        out =self.bash("Xvfb $DISPLAY &")
        for lin in out:
            print(lin.strip())
        

    def openTerminal(self):
        if self.state == states[0]:
            bash('save="DISPLAY"')
            bash("export DISPLAY=:44 ")
            bash("Xvfb $DISPLAY &")
            return 0
        return 1

    def bash(self, command):
        self.proc.stdin.open()
        self.proc.stdin.write(command)
        self.proc.stdin.close()
        return self.proc.stdout

if __name__ == "__main__":
    eggnogg = EggnoggInterface()