# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile.config import Key,Screen, Group, Match, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from libqtile.config import EzKey
mod="mod4"
font="NovaRound"
EzKey.modifier_keys = {
                'M': 'mod4',
                'A': 'mod1',
                'S': 'shift',
                'C': 'control',
                }
color = [["#002b36","#002b36"],#BG  [0]
         ["#002b36","#002b36"],#0   [1]
         ["#dc322f","#dc322f"],#1   [2]
         ["#859900","#859900"],#2   [3]
         ["#b58900","#b58900"],#3   [4]
         ["#268bd2","#268bd2"],#4   [5]
         ["#6c71c4","#6c71c4"],#5   [6]
         ["#2aa198","#2aa198"],#6   [7]
         ["#93a1a1","#93a1a1"],#7   [8]
         ["#93a1a1","#93a1a1"],#FG  [9]
         ["#657b83","#657b83"],#8   [10]
         ["#cb4b16","#cb4b16"],#9   [11]
         ["#859900","#859900"],#10  [12]
         ["#b58900","#b58900"],#11  [13]
         ["#2aa198","#2aa198"],#12  [14]
         ["#d33882","#d33882"],#13  [15]
         ["#2aa198","#2aa198"],#14  [16]
         ["#fdf6e3","#fdf6e3"]]#15  [17]
keys = [
    # Switch between windows in current stack pane
    EzKey("M-k",   lazy.layout.down()),
    EzKey("M-j",   lazy.layout.up()),
    # Move windows up or down in current stack
    EzKey("M-S-k", lazy.layout.shuffle_down()),
    EzKey("M-S-j", lazy.layout.shuffle_up()),
    EzKey("M-h",   lazy.layout.grow(),  # Grow size of current window (XmonadTall)
    
                 lazy.layout.increase_nmaster(),         # Increase number in master pane (Tile
       ),
    EzKey("M-l",   lazy.layout.shrink(),   # Shrink size of current window (XmonadTall)
                 lazy.layout.decrease_nmaster()         # Decrease number in master pane (Tile)
       ),
    EzKey("M-n",   lazy.layout.normalize()                 # Restore all windows to default size ratios
       ),
    EzKey("M-S-f", lazy.window.toggle_floating()           # Toggle floating
       ),
    # Switch window focus to other pane(s) of stack
    EzKey("M-<space>",  lazy.layout.next()),
    EzKey("M-f",   lazy.window.toggle_fullscreen()),
    # Swap panes of split stack
    EzKey("M-S-<space>",lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    EzKey("M-S-<Return>", lazy.layout.toggle_split()),
    EzKey("M-b",   lazy.spawn("firefox")),
    # Toggle between different layouts as defined below
    EzKey("M-<Tab>",   lazy.next_layout()),
    EzKey("M-S-<Tab>", lazy.prev_layout()),
    EzKey("M-c",   lazy.spawn("compton --config /home/parsrch/.config/qtile/compton.conf")),
    EzKey("M-<Return>",   lazy.spawn("alacritty")),
    EzKey("M-s",   lazy.spawn("spotify")),
    EzKey("M-m",   lazy.spawn("minecraft-launcher")),
    EzKey("M-S-c", lazy.spawn("killall compton")),
    EzKey("M-v",   lazy.spawn("vlc")),
    EzKey("<XF86AudioRaiseVolume>",   lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    EzKey("<XF86AudioLowerVolume>",   lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    EzKey("<XF86AudioPlay>",   lazy.spawn("playerctl play-pause")),
    EzKey("<XF86AudioPause>",   lazy.spawn("playerctl pause")),
    EzKey("<XF86AudioNext>",   lazy.spawn("playerctl next")),
    EzKey("<XF86AudioPrev>",   lazy.spawn("playerctl previous")),
    EzKey("A-q",   lazy.spawn("xkill")),
    EzKey("<Print>",   lazy.spawn("flameshot gui")),
    EzKey("M-t",   lazy.spawn("telegram-desktop")),
    EzKey("M-d",   lazy.spawn("discord")),
    EzKey("M-e",   lazy.spawn("alacritty -e 'ranger'")),
    EzKey("A-e",   lazy.spawn("pcmanfm")),
    EzKey("M-q",   lazy.window.kill()),
    EzKey("M-C-r", lazy.restart()),
    EzKey("M-C-q", lazy.shutdown()),
    EzKey("M-r",   lazy.spawn("rofi -theme rofi/appmenu/drun.rasi -show drun")),
]
groups = [
          Group("ï¶", matches=[Match(wm_class=["minecraft-launcher","Wine"])]),
          Group("ï¤‡",matches=[Match(wm_class=["firefox","qutebrowser","surf"])]),
          Group("ï¾", matches=[Match(wm_class=["TelegramDesktop","discord"])]),
          Group("ïŒ‚", matches=[Match(wm_class=["gimp-2.10","Blender","Spotify","vlc"])]),
          Group("ï»", matches=[Match(wm_class=["Pcmanfm"],title=["ranger"])]),
          Group("ï…"),
                    ]
# allow mod3+1 through mod3+0 to bind to groups; if you bind your groups
# by hand in your config, you don't need to do this.
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)
layout_theme = {"border_width": 2,
                "margin": 5,
                "border_focus": "b58900", 
                "border_normal":"073642" 
                }

layouts = [        
   layout.Max(**layout_theme),
     #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
     #layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
     layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
     layout.RatioTile(**layout_theme),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
     layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font=font,
    fontsize=12,
    padding=3,
    foreground=color[17],
    background=color[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=color[6]),
                widget.Image(filename="~/.config/qtile/[6].png"),
                widget.GroupBox(background=color[8]),
                widget.Image(filename="~/.config/qtile/[8].png"),
                widget.WindowName(background=color[1],show_state=False),
                widget.Image(filename="~/.config/qtile/[5].png"),
                widget.Systray(background=color[5]),
                widget.Image(filename="~/.config/qtile/[14].png"),
                widget.ThermalSensor(background=color[14],fmt="ï‹‡{}",tag_sensor="Tctl"),
                widget.Image(filename="~/.config/qtile/[3].png"),
                widget.Net(background=color[3],interface="enp39s0",fontsize=9,format="{down} â†“â†‘ {up}"),
                widget.Image(filename="~/.config/qtile/[4].png"),
                widget.CheckUpdates(background=color[4],distro="Arch_yay",display_format="ï€¡ {updates}"),
                widget.Image(filename="~/.config/qtile/[11].png"),
                widget.Volume(background=color[11]),
                widget.Image(filename="~/.config/qtile/[2].png"),
                widget.Clock(background=color[2],format='%d %a %I:%M %p'),
                ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
            Drag([mod], "Button1", lazy.window.set_position_floating(),
                         start=lazy.window.get_position()),
                Drag([mod], "Button3", lazy.window.set_size_floating(),
                             start=lazy.window.get_size()),
                    Click([mod], "Button2", lazy.window.bring_to_front())
                    ]
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp =True 
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
@hook.subscribe.startup_once
def start_once():
        home = os.path.expanduser('~')
        subprocess.call([home + '/.config/qtile/autostart.sh'])
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"

