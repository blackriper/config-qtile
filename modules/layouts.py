from libqtile import layout
from libqtile.config import Match
from .theme import colors 

#Layouts and layouts rules 

layout_conf={
   'border_focus':colors['focus'][0],
   'border_width':3,
   'margin':9
}


layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2,**layout_conf),
    layout.RatioTile(**layout_conf),
    #layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
  border_focus=colors["color4"][0]
)
