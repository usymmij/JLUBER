#!/bin/bash
LC_ALL=C
# all paresed files are ascii, so this will speed up the 
# string parsers

leave=false
arr=("closed", "main", "maps", "game", "esc" )
declare -i id=$1
idchar=$1
SOURCE="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

value=""

# save original X display number


# args: The message to write to buffer
function writeBuffer() {
    echo $id env $1 >> $SOURCE/hello.buffer
}

function readBuffer() {
    value=$(grep "^$id gym " $SOURCE/hello.buffer | head -1)
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
    if echo "$2" | grep -q "d $1" ; then
        xdotool keydown "$1"
    fi
    if echo "$2" | grep -q "u $1" ; then
        xdotool keyup --delay 250 "$1"
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
readBuffer

for (( ; ; ))
do
    readBuffer
    if [ -n "$value" ]
    then
        checkKey "p" "$value"

        checkKey "w" "$value"
        checkKey "s" "$value"
        checkKey "a" "$value"
        checkKey "d" "$value"
        checkKey "b" "$value"
        checkKey "v" "$value"

        checkKey "i" "$value"
        checkKey "j" "$value"
        checkKey "k" "$value"
        checkKey "l" "$value"
        checkKey "n" "$value"
        checkKey "u" "$value"
    fi    
done
#kill the process
#killPs



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
