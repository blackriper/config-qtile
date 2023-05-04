from libqtile import widget
from libqtile import qtile
from .keys import terminal
from .theme import colors
from scripts import diskspace,Spotify
import os


#settings defaults
widget_defaults = dict(
    font='FiraCode Nerd Font',
    fontsize=11,
    padding=1,
)
extension_defaults = widget_defaults.copy()

#auxilar widgets
def base_color(fg='text',bg='dark'):
    return {
        'foreground':colors[fg],
        'background':colors[bg]
    }

def separator(pd=2):
    return widget.Sep(
                  **base_color(fg='color1'),
                  linewidth=2,
                  margin=8,
                  size_percent=80,
                  padding=pd)

def nerd_icon(fg='text',bg='dark',text="?"):
    return widget.TextBox(
                **base_color(fg,bg),
                font='Iosevka Nerd Font ',
                fontsize=17,
                text=text,
                padding=5)

def open_gtop():
    return qtile.cmd_spawn(f"{terminal} -e gtop")


def workspaces():
    return[
        widget.Sep(**base_color('text','dark'),linewidth=0,padding=6),
        widget.GroupBox(
               highlight_method='text',
               this_screen_border=colors['grey'],
               this_current_screen_border=colors['focus2'],
               other_current_screen_border=colors['dark'],
               other_screen_border=colors['focus2'],
               urgent_alert_method='text',
               urgen_border=colors['color4'],
               active=colors['focus1'],
               inactive=colors['light'],
               rounded=False,
               background=colors['dark'],
               disable_drag=True),
        widget.WindowName(**base_color(fg='focus'), fontsize=11 ,padding=5),
       ]



primary_widgets = [
        *workspaces(),
        widget.Spacer(size_percent=60),
        widget.CurrentLayoutIcon(scale=0.55),
        widget.CurrentLayout(**base_color(fg='light'), padding=5),
        separator(),
        nerd_icon(fg='color1',text='  '),
        widget.CheckUpdates(
               update_interval=1800,
               distro="Arch_yay",
               no_update_string="0 Updates",
               display_format="{updates} Updates",
               colour_have_updates=colors['color3'],
               colour_no_updates=colors['light'],
               mouse_callbacks={
                    'Button1':
                    lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                }),
        separator(pd=7),
        nerd_icon(fg='focus2',text=" 󰏈 "),
        widget.ThermalSensor(
                      **base_color(fg='light'),
                      mouse_callbacks = {
                          'Button1': lambda : open_gtop()
                      }),
        nerd_icon(fg='color3',text=" 󰍛 "),
        widget.Memory(
                format = "{MemUsed:.0f}{mm}",
                **base_color(fg='light'),
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda :  open_gtop()
                }
            ),
        widget.Spacer(length=5),
        separator(pd=12),
        Spotify(format=("{icon} : {track}")),
        nerd_icon(fg='focus1',text='  '),
        widget.Bluetooth(
            hci='/dev_90_7A_58_1B_8B_C6',
            **base_color(fg='light'),
             mouse_callbacks={
                    'Button1':
                     lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/scripts/rofi-bluetooth'))
               }),
        nerd_icon(fg='color3',text='  '),
        widget.Volume(
               **base_color(fg='light'),
               mouse_callbacks={
                    'Button1':
                     lambda: qtile.cmd_spawn("pavucontrol")
               }),
        widget.Spacer(length=5),
        separator(),
        nerd_icon(fg='color4',text=' 󰃰 '),
        widget.Clock(
                    format='%d/%m/%Y - %I:%M %p',
                    **base_color(fg='light')),
        widget.Spacer(length=9),
        widget.Systray(icon_size = 20),


]


secondary_widgets=[
        *workspaces(),
        widget.Spacer(size_percent=60),
        widget.CurrentLayoutIcon(scale=0.55),
        widget.CurrentLayout(**base_color(fg='light'), padding=5),
        separator(),
        nerd_icon(fg='color3',text=" 󰘚 "),
        widget.CPU(
                format = "{load_percent}%",
                **base_color(fg='light'),
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda :  open_gtop()
                }
            ),
        nerd_icon(fg='color4',text="  "),
        widget.GenPollText(
                **base_color(fg='light'),
                update_interval = 5,
                func = lambda: diskspace('FreeSpace'),
                mouse_callbacks = {
                    'Button1': lambda :  open_gtop()
                }
            ),
        separator(pd=12),
        widget.OpenWeather(
               cityid="4012721",
               **base_color(fg='light'),
               format=("{icon} {location_city} : {main_temp} °{units_temperature}"),
               mouse_callbacks={
                     'Button1':
                      lambda: qtile.cmd_spawn("brave -o https://openweathermap.org/city/4012721")
                }),
        separator(pd=7),
        nerd_icon(fg='color2',text=' '),
        widget.Spacer(length=5),
        widget.Net(**base_color(fg='light'), interface='wlan0'),
        widget.Spacer(length=5),
        separator(),
        nerd_icon(fg='color4',text=' 󰃰 '),
        widget.Clock(
                    format='%d/%m/%Y - %I:%M %p',
                    **base_color(fg='light')),

]
