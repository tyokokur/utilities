#!/bin/bash

## TJY Modified auto-update to Github folder

## Pause using: ctrl+z
## Kill all paused: $ kill -9 $(jobs -p)
## Source: https://jakemccrary.com/blog/2020/02/25/auto-syncing-a-git-repository/

set -e

TARGETDIR=("D:\(000) Git")

stderr () {
    echo "$1" >&2
}

is_command() {
    command -v "$1" &>/dev/null
}

INW="inotifywait";
EVENTS="modify,move,delete,create";

for cmd in "git" "$INW" "timeout"; do
    is_command "$cmd" || { stderr "Error: Required command '$cmd' not found"; exit 1; }
done

INCOMMAND="\"$INW\" -qr -e \"$EVENTS\" --exclude \"\.git\" \"$TARGETDIR\"";
echo "$INCOMMAND"

while true; do
    NOW=$(date)
    eval "timeout 600 $INCOMMAND" || true
    for i in $(ls -d */); do
        cd "$TARGETDIR/$i"
        echo $i
        git pull
        sleep 5
        STATUS=$(git status -s)
        if [ -n "$STATUS" ]; then
            echo "$STATUS"
            echo "commit!"
            git add .
            git commit -m "autocommit"
            git push origin
        fi
    done
    ## Print when done looping
    echo ""
    echo "/********** Loop end **********/"
    echo "-----Waiting for 10 minutes-----"
    echo "--Next auto-run: $($NOW -d "+10 minutes")--"
done