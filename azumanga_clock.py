#!/usr/bin/python3

import gi
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

def get_screen_size(display):
    mon_geoms = [
        display.get_monitor(i).get_geometry()
        for i in range(display.get_n_monitors())
    ]

    x0 = min(r.x            for r in mon_geoms)
    y0 = min(r.y            for r in mon_geoms)
    x1 = max(r.x + r.width  for r in mon_geoms)
    y1 = max(r.y + r.height for r in mon_geoms)

    return x1 - x0, y1 - y0

print(int(time.strftime('%H')))
def get_clock_text():
    time_text = time.strftime('         今日は:\n      %A\n    %H:%M:%S')
    hour_of_day = int(time.strftime('%H'))
    if hour_of_day >= 5 and hour_of_day < 12:
        greeting_text = "       おはよう！\n"
    elif hour_of_day < 5 and hour_of_day >= 0:
        greeting_text = "       おやすみ！\n"
    elif hour_of_day >= 12 and hour_of_day <= 17:
        greeting_text = "      こんにちは！\n"
    elif hour_of_day > 17 and hour_of_day <= 24:
        greeting_text = "      こんばんは！\n"
    else:
        greeting_text = "            よー.\n" 
    return("<span size='5500'>{}</span><span size='7000'>{}</span>".format(greeting_text,time_text))

class azumangaClock:
    def __init__(self):
        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        self.overlay = Gtk.Overlay()
        win.add(self.overlay)
        self.img = Gtk.Image.new_from_file('/home/shawn/Downloads/azumanga_clock.gif')
        self.overlay.add(self.img)
        self.label=Gtk.Label()
        self.label.set_markup(get_clock_text())
        self.label.set_line_wrap(True)
#self.label.set_justify(Gtk.Justification.LEFT)
        self.label.set_valign(Gtk.Align.CENTER)
        self.label.set_halign(Gtk.Align.START)
        self.overlay.add_overlay(self.label)
        self.overlay.show_all()
        win.set_type_hint(Gdk.WindowTypeHint.UTILITY)
        win.set_decorated(False)
        win.set_gravity(Gdk.Gravity.SOUTH_EAST)
        w_h = get_screen_size(Gdk.Display.get_default())
        width = w_h[0]
        height = w_h[1]
        
        window_w_h = win.get_size()
        win_width = window_w_h[0]
        win_height = window_w_h[1]
        print(win.get_gravity())
        win.move(width - win_width, height - win_height - 20)
        win.show_all()
    
    def update(self):
        self.label.set_markup(get_clock_text())
        return True

def main():
    Gtk.main()

if __name__ == "__main__":
    clock = azumangaClock()
    GLib.timeout_add(1000, clock.update)
    main()
    
#win = Gtk.Window()
#win.connect("destroy", Gtk.main_quit)
#overlay = Gtk.Overlay()
#win.add(overlay)
#img = Gtk.Image.new_from_file('/home/shawn/Downloads/azumanga_clock.gif')
#overlay.add(img)
#
#
#label = make_time_label()
#overlay.add_overlay(label)
#overlay.show_all()
#
#win.set_type_hint(Gdk.WindowTypeHint.UTILITY)
#win.set_decorated(False)
#win.show_all()
#Gtk.main()
#

