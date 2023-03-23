#!/bin/sh
# resolucion of monitors
xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x1080 --output HDMI-1 --mode 1360x768 --pos 0x0

#Background 
feh -z --bg-scale ~/Imágenes/*
py scripts/cron.py &

#Trasparency 
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

#Network icon and Usb icon 
nm-applet &
udiskie -t -f thunar &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

