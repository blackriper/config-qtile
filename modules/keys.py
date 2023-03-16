# Qtile keybindings

from libqtile.lazy import lazy
from libqtile.config import Key
import os

mod = "mod4"
terminal = "alacritty"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod],"space",lazy.layout.next()),

     # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

     # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    #Menu
    ([mod], "r", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "r", lazy.spawn("rofi -show")),

    #Power Menu
    ([mod], "x", lazy.spawn(os.path.expanduser('~/.config/rofi/scripts/powermenu.sh'))),

    # Browser Brave
    ([mod], "b", lazy.spawn("brave")),

    # Visual Studio code
    ([mod], "v", lazy.spawn("code")),
    
     # Sublime text
    ([mod], "z", lazy.spawn("subl")),

    # Microsoft Edge
    ([mod], "m", lazy.spawn("microsoft-edge-stable")),

    # Spoify
    ([mod], "s", lazy.spawn("spotify")),

    #whatshapp
    ([mod],"F10",lazy.spawn("whatsapp-for-linux")),

    # File Explorer
    ([mod], "t", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn(terminal)),

    # Redshift
    ([mod], "F1", lazy.spawn("redshift -O 2400")),
    ([mod], "F9", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "Print", lazy.spawn(os.path.expanduser('~/.config/rofi/scripts/screenshot.sh'))),
    ([mod, "shift"], "Print", lazy.spawn(os.path.expanduser('~/.config/rofi/scripts/screenshot.sh 1'))),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    ([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    ([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
