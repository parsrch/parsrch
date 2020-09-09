#! /bin/bash 
compton --config ~/.config/qtile/compton.conf &
nitrogen --restore &
setxkbmap -layout us,ir && setxkbmap -option 'grp:alt_shift_toggle' &
/usr/lib/xfce4/notifyd/xfce4-notifyd
#nm-applet
