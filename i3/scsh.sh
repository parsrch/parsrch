#!/bin/bash
killall xfce4-screenshooter;xfce4-screenshooter -c -s ~/shots/$(date +"%Y-%m-%d|%H:%M:%S").png -r
