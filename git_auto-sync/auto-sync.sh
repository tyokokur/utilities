#!/bin/bash

########################

## ORIGINAL: Last edit 20220809

########################

## TJY Modified auto-update to Github folder
## Pause using: ctrl+z
## Kill all paused: $ kill -9 $(jobs -p)
## Source: https://jakemccrary.com/blog/2020/02/25/auto-syncing-a-git-repository/

set -e

## Parent directory to check through -- all folders must be git clones
TARGETDIR=("E:\(000) Git")

stderr () {
    echo "$1" >&2
}

is_command() {
    command -v "$1" &>/dev/null
}

INW="inotifywait";
EVENTS="modify,move,delete,create";

## Error checking
for cmd in "git" "$INW" "timeout"; do
    is_command "$cmd" || { stderr "Error: Required command '$cmd' not found"; exit 1; }
done

## Loop through all folders in parent
sync_children(){
    cd "$1"
    for i in $(ls -d */); do
        cd "$1/$i"
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
}

## Initial sync
sync_children "$TARGETDIR"

## Sync on change
INCOMMAND="\"$INW\" -qr -e \"$EVENTS\" --exclude \"\.git\" \"$TARGETDIR\"";
while true; do
    echo ""
    echo "/********** Loop start **********/"
    echo "$INCOMMAND"
    echo "$(date)"
    eval "timeout 600 $INCOMMAND" || true

    SECONDS=0
    sync_children "$TARGETDIR"

    ## Print when done looping
    echo ""
    echo "/********** Loop end **********/"
    echo "/** Duration: $SECONDS seconds **/"
    echo "--Next auto-run: $(date -d "+10 minutes")--"
done