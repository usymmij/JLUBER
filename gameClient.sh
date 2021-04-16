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
function writeBuffer() {
    echo $id env $1 >> $SOURCE/hello.buffer
}

function readBuffer() {
    value=$(grep "^$id gym " $SOURCE/hello.buffer | tail -1)
    if [ -n "$value" ]
    then
        grep -v "$value" $SOURCE/hello.buffer > temp && mv temp $SOURCE/hello.buffer
    fi
}

function startUp() {
    xdotool key --delay 150 "b"
    sleep 0.3
    xdotool key --delay 150 "b"
    sleep 4
}

function checkKey() {
    if grep -q $1 "$2"; then
        xdotool keydown $1
    else
        xdotool keyup $1
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
writeBuffer "booted"

readBuffer

python3 ../../scrnsht.py
#kill the process
killPs



#for (( ; ; ))
#do
#    
#    if [ leave ]
#    
#    then
#	    break       	   #Abandon the loop.
#    fi
#
#done
