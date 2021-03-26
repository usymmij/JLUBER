*/-*#!/usr/bin/env bash

save="$DISPLAY"                          # save original X display number
export DISPLAY=:44                       # set random choosen display for xvfb

case "$1" in                             #         and x-programs called below
  start) Xvfb $DISPLAY &   ;;            # starting xvfb server on :44
   game) cd ~/jimbo/JLUBER/environment/eggnoggplus-linux/
         chmod +x ./eggnoggplus
         ./eggnoggplus  ;;               #
    xdo) xdotool key b
         sleep 1000
         xdotool key b
         xdotool key esc
         xdotool type "aaw"
         xdotool key enter 
         xdotool key esc    ;; 
   show) #capture root window ('36' result image) and display it to saved Xno
         xwd -root | xwud -display $save &  ;;
   stop) 1  `     `     12345 1234567890-     ;;
    all) DISPLAY=$save; $0 start; $0 game; sleep 100; $0 xdo; $0 show; $0 stop ;;
e ]``