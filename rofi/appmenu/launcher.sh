#!/usr/bin/env bash

## Author  : Aditya Shakya
## Mail    : adi1090x@gmail.com
## Github  : @adi1090x
## Twitter : @adi1090x

# Available Styles
# >> Created and tested on : rofi 1.6.0-1
#
# slate_full     slate_center     slate_left
# slate_right    slate_top        slate_bottom

theme="slate_center"

dir="$HOME/.config/rofi/appmenu"
styles=($(ls -p --hide="colors.rasi" $dir/styles))
color="Nord.rasi"

# comment this line to disable random colors
sed -i -e "s/@import .*/@import \"$color\"/g" $dir/styles/colors.rasi

# comment these lines to disable random style
themes=($(ls -p --hide="launcher.sh" --hide="styles" $dir))

rofi -show drun -modi drun -theme $dir/"$theme" -hover-select -me-select-entry '' -me-accept-entry 'MousePrimary'
