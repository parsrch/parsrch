#! /bin/bash 
compton --config ~/.config/qtile/compton.conf &
nitrogen --restore &
setxkbmap -layout us,ir && setxkbmap -option 'grp:alt_shift_toggle'
#nm-applet
