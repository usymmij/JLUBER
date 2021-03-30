#!/usr/bin/env bash

cd ~/jimbo/JLUBER/environment/eggnoggplus-linux/
./eggnoggplus &

echo "waiting"
sleep 0.25

xdotool activatewindow eggnoggplus

sleep 0.2
xdotool key type "bbbb"
sleep 2
xdotool key type "bbbbwasbddddbbdbdbdbdbdb"

xdotool key --delay 500 "b"
sleep 0.6
xdotool key --delay 500 "b"
sleep 0.6
xdotool key --delay 500 "b"
sleep 0.6
xdotool key --delay 500 "b"
echo "hit b"
sleep 5
xdotool key --delay 500 "b"
echo "hit b"
sleep 0.6
xdotool key --delay 500 "Escape"
echo "escape"
sleep 0.6
xdotool key --delay 500 "s"
sleep 0.6
xdotool key --delay 500 "a"
sleep 0.6
xdotool key --delay 500 "w"
sleep 0.6
xdotool key --delay 500 "b"
echo "typed sawb"
sleep 0.6
xdotool key --delay 500 "Escape"
echo "escape"
exit