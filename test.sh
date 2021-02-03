#!/usr/bin/env bash

cd ~/jimbo/JLUBER/environment/eggnoggplus-linux/
./eggnoggplus &

sleep 0.75

xdotool key --delay 150 "b"
sleep 0.3
xdotool key --delay 150 "b"
sleep 3
xdotool key --delay 150 "Escape"
sleep 0.3
xdotool key --delay 150 "s"
sleep 0.3
xdotool key --delay 150 "a"
sleep 0.3
xdotool key --delay 150 "w"
sleep 0.3
xdotool key --delay 150 "b"
sleep 0.3
xdotool key --delay 150 "Escape"