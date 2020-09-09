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
color = [["#2e3440","#2e3440"],#BG  [0]
         ["#2e3440","#2e3440"],#0   [1]
         ["#bf616a","#bf616a"],#1   [2]
         ["#a3be8c","#a3be8c"],#2   [3]
         ["#ebcb8b","#ebcb8b"],#3   [4]
         ["#5e81ac","#5e81ac"],#4   [5]
         ["#b48ead","#b48ead"],#5   [6]
         ["#8fbcbb","#8fbcbb"],#6   [7]
         ["#4c566a","#4c566a"],#7   [8]
         ["#4c566a","#4c566a"],#FG  [9]
         ["#3b4252","#3b4252"],#8   [10]
         ["#d08770","#d08770"],#9   [11]
         ["#a3be8c","#a3be8c"],#10  [12]
         ["#ebcb8b","#ebcb8b"],#11  [13]
         ["#8fbcbb","#8fbcbb"],#12  [14]
         ["#b48ead","#b48ead"],#13  [15]
         ["#8fbcbb","#8fbcbb"],#14  [16]
         ["#fdf6e3","#fdf6e3"]]#15  [17]
keys = [
    # Switch between windows in current stack pane
    EzKey("M-k",                lazy.layout.down()),
    EzKey("M-j",                lazy.layout.up()),
    # Move windows up or down in current stack
    EzKey("M-S-k",              lazy.layout.shuffle_down()),
    EzKey("M-S-j",              lazy.layout.shuffle_up()),
    EzKey("M-h",                lazy.layout.grow(),  # Grow size of current window (XmonadTall)
                                lazy.layout.increase_nmaster(),         # Increase number in master pane (Tile
       ),
    EzKey("M-l",                lazy.layout.shrink(),   # Shrink size of current window (XmonadTall)
                                lazy.layout.decrease_nmaster()         # Decrease number in master pane (Tile)
       ),
    EzKey("M-n",                lazy.layout.normalize()                 # Restore all windows to default size ratios
       ),
    EzKey("M-S-f",              lazy.window.toggle_floating()           # Toggle floating
       ),
    # Switch window focus to other pane(s) of stack
    EzKey("M-<space>",          lazy.layout.next()),
    EzKey("M-f",                lazy.window.toggle_fullscreen()),
    # Swap panes of split stack
    EzKey("M-S-<space>",        lazy.layout.rotate()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    EzKey("M-S-<Return>",       lazy.layout.toggle_split()),
    EzKey("M-b",                lazy.spawn("qutebrowser")),
    # Toggle between different layouts as defined below
    EzKey("M-<Tab>",            lazy.next_layout()),
    EzKey("M-S-<Tab>",          lazy.prev_layout()),
    EzKey("M-c",                lazy.spawn("compton --config .config/compton/compton.conf")),
    EzKey("M-<Return>",         lazy.spawn("alacritty")),
    EzKey("M-s",                lazy.spawn("spotify")),
    EzKey("M-m",                lazy.spawn("minecraft-launcher")),
    EzKey("M-S-c",              lazy.spawn("killall compton")),
    EzKey("M-v",                lazy.spawn("vlc")),
    EzKey("<XF86AudioPlay>",    lazy.spawn("playerctl play-pause")),
    EzKey("M-<bracketleft>",    lazy.spawn("playerctl next")),
    EzKey("M-<semicolon>",      lazy.spawn("playerctl previous")),
    EzKey("M-p",                lazy.spawn("playerctl play-pause")),
    EzKey("<XF86AudioPause>",   lazy.spawn("playerctl pause")),
    EzKey("<XF86AudioNext>",    lazy.spawn("playerctl next")),
    EzKey("<XF86AudioPrev>",    lazy.spawn("playerctl previous")),
    EzKey("A-q",                lazy.spawn("xkill")),
    EzKey("M-<Print>",          lazy.spawn("scrot -q 100 '%Y-%m-%d_%H:%m:%S.png' -e 'mv $f ~/shots/'")),
    EzKey("M-t",                lazy.spawn("telegram-desktop")),
    EzKey("M-d",                lazy.spawn("discord")),
    EzKey("M-e",                lazy.spawn("alacritty -e 'vifm'")),
    EzKey("A-e",                lazy.spawn("pcmanfm")),
    EzKey("M-q",                lazy.window.kill()),
    EzKey("M-C-r",              lazy.restart()),
    EzKey("M-C-q",              lazy.shutdown()),
    EzKey("M-r",                lazy.spawn("rofi -theme rofi/appmenu/drun.rasi -show drun")),
]
layout_theme = {"border_width": 2,
                "margin": 7,
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
groups = [
          Group("1",label="",matches=[Match(wm_class=["minecraft-launcher","Wine"])],layout="max"),
          Group("2",label="龜",matches=[Match(wm_class=["firefox","qutebrowser","surf"])],layout="monadtall"),
          Group("3", label="",matches=[Match(wm_class=["TelegramDesktop","discord"])],layout="max"),
          Group("4", label="",matches=[Match(wm_class=["gimp-2.10","Blender","Spotify","vlc"])],layout="max"),
          Group("5", label="",matches=[Match(wm_class=["Pcmanfm"],title=["vifm"])],layout="monadtall"),
          Group("6",label="",layout="monadtall"),
                    ]
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)

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
                widget.GroupBox(background=color[8],inactive=color[1],this_current_screen_border=color[4],urgent_border=color[2],borderwidth=2,),
                widget.Image(filename="~/.config/qtile/[8].png"),
                widget.WindowName(background=color[1],show_state=False),
                widget.Image(filename="~/.config/qtile/[5].png"),
                widget.Systray(background=color[5]),
                widget.Image(filename="~/.config/qtile/[14].png"),
                widget.ThermalSensor(background=color[14],fmt="{}",tag_sensor="Tctl"),
                widget.Image(filename="~/.config/qtile/[3].png"),
                widget.Net(background=color[3],interface="enp39s0",fontsize=9,format="{down} ↓↑ {up}"),
                widget.Image(filename="~/.config/qtile/[4].png"),
                widget.CheckUpdates(background=color[4],distro="Arch_yay",display_format=" {updates}"),
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
cursor_warp =False
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
        subprocess.call([home + '/.config/autostart.sh'])
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
