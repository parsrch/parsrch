#! /usr/bin/bash
compton --config ~/.config/compton/compton.conf &
nitrogen --restore &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
setxkbmap -v workman,ir-parsarch && xset r 66  && setxkbmap -option 'grp:alt_shift_toggle' &&setxkbmap -option caps:backspace &
killall volumeicon;volumeicon &
killall nm-applet;nm-applet&
#killall conky;
#conky -c ~/.config/conky/syclo/syclo-orange-bottomleft.conkyrc &
#conky -c ~/.conky/conky-spotify/conky-spotify-medium
#xinput --set-button-map 8 3 2 1
searx-run
