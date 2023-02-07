#!/bin/bash

broadwayd -p 8080 :3 &
#export GDK_BACKEND=broadway
#export BROADWAY_DISPLAY=:3
#gnome-terminal
export GDK_BACKEND=broadway && export BROADWAY_DISPLAY=:3 && python /mnt/d/box/ho/py.py
