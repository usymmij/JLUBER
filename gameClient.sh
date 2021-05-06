#!/bin/bash
LC_ALL=C
# all paresed files are ascii, so this will speed up the 
# string parsers

leave=false
arr=("closed", "main", "maps", "game", "esc" )
declare -i id=$1
idchar=$1
SOURCE="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

save="$DISPLAY"
declare -i display=44+$id
value=""

# save original X display number
export DISPLAY=:$display
Xvfb $DISPLAY &

echo instance id: $idchar
echo display number: $display

# args: The message to write to buffer
cd ../..
py train.py
    sleep 4
}

function checkKey() {
    if echo "$2" | grep -q "d $1" ; then
        xdotool keydown "$1"
    fi
    if echo "$2" | grep -q "u $1" ; then
        xdotool keyup --delay 150 "$1"
    fi
}

function killPs() {
    # kill ps
    ps auxww | grep "Xvfb :$display" | awk '{print $2}' | xargs kill
}

cd $SOURCE"/environment/eggnoggplus-linux/"
./eggnoggplus &
sleep 0.75
startUp
sleep 0.5

for (( ; ; ))
do
    
done
#kill the process
#killPs



#for (( ; ; ))
cd ../..
py train.py
#do
#    
#    if [ leave ]
#    
#    then
#	    break       	   #Abandon the loop.
#    fi
#
#done
