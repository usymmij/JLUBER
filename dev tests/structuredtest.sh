#!/usr/bin/env bash
save="$DISPLAY"                          # save original X display number
export DISPLAY=:44  
Xvfb $DISPLAY &


cd ~/jimbo/JLUBER/environment/eggnoggplus-linux/
./eggnoggplus &

sleep 0.75

xdotool key --delay 150 "b"
sleep 0.3
xdotool key --delay 150 "b"
sleep 0.3
xdotool key --delay 150 "Escape"
xwd -root | xwud -display $save & 
sleep 0.3
xdotool key --delay 150 "s"
sleep 0.3
xdotool key --delay 150 "a"
sleep 0.3
xdotool key --delay 150 "w"
sleep 0.3
xdotool key --delay 150 "b"
xwd -root | xwud -display $save & 
sleep 0.3
xdotool key --delay 150 "Escape"
ps auxww | grep "Xvfb :44" | awk '{print $2}' | xargs kill