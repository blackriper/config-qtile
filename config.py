from modules.layouts import layouts, floating_layout
from modules.widgets import widget_defaults,extension_defaults
from modules.keys import keys, mod
from modules.groups import groups
from modules.screens import screens
from modules.mouse import mouse
from modules.hooks import *
import os

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "urgent"
wmname = "Qtile"

