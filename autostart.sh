#! /usr/bin/bash
picom &
nitrogen --restore &
/usr/lib64/xfce4/notifyd/xfce4-notifyd &
setxkbmap -v workman,ir-parsarch && xset r 66  && setxkbmap -option 'grp:alt_shift_toggle' &&setxkbmap -option caps:backspace && setxkbmap -option shift:both_capslock
sh ~/.config/polybar/launch.sh&
killall xfce4-clipman;
xfce4-clipman &
killall volumeicon;
volumeicon &

