#!/usr/bin/env python3

## License: GPL (c) 2016
##
## Update of my simple script for controlling Kodi from the computer
## my first intent with GTK3 and I use it to learn about GTK3 and python3
## Tomas Kaluza

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
## Use the following if you want to use Gtk.Clipboard
#from gi.repository import Gtk, Gdk
import subprocess


class GridWindow(Gtk.Window):

    def __init__(self):
        try:
            self.clipboard_value=subprocess.check_output(["xclip", "-o"])
            ## Use the following if you want to use Gtk.Clipboard
            #self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
            #self.clipboard_value = self.clipboard.wait_for_text()
        except:
            #self.clipboard_value="b''"
            self.clipboard_value = bytes()
        try:
            self.clipboard_value = (self.clipboard_value.decode('ascii'))
            ## Following works as well,but not sure it it is needed at all
            #self.clipboard_value=(clipboard_value.decode('utf-8'))
            ## Use the following if you want to use Gtk.Clipboard
            #self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
            #self.clipboard_value = self.clipboard.wait_for_text()
        except:
            #self.clipboard_value="b''"
            self.clipboard_value = bytes()


        Gtk.Window.__init__(self, title="Send YouTube link to Kodi using kodi-cli")
        self.set_border_width(8)
        grid = Gtk.Grid()
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        self.add(grid)

        self.youtube_entry = Gtk.Entry(text=self.clipboard_value)
        #youtube_entry.set_text("Hello World")
        self.progressbar = Gtk.ProgressBar(text="Kodi is not playing at the moment")
        self.progresseventbox = Gtk.EventBox()
        self.progressbar.set_show_text(True)
        self.add_to_playlist = Gtk.Button(label="Add to playlist")
        self.toggle_fullscreen = Gtk.Button(label="Toggle fullscreen")
        self.toggle_playpause = Gtk.Button(label="Toggle Play / Pause")
        self.play_now = Gtk.Button(label="Play link now")
        self.output_text = Gtk.Label(self, label="kodi-cli output")
        #output_text = Gtk.Label(output)
        

        #grid.add(youtube_entry)
        grid.attach(self.youtube_entry, 0, 0, 4, 1)
        # Let's add the eventbox and inside the progress bar instead of just adding the progress bar
        #grid.attach_next_to(self.progressbar, self.youtube_entry, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(self.progresseventbox, self.youtube_entry, Gtk.PositionType.BOTTOM, 4, 1)
        self.progresseventbox.add(self.progressbar)
        pbsize = self.progressbar.get_allocation()
        print("here I am")
        print(pbsize)
        print(pbsize.width)
        #print(event.x)
        #self.progressbar.set_fraction(0.20)
        grid.attach_next_to(self.add_to_playlist, self.progresseventbox, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.toggle_fullscreen, self.add_to_playlist, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.toggle_playpause, self.toggle_fullscreen, Gtk.PositionType.RIGHT, 1, 1)
        #grid.attach(button5, 3, 2, 1, 1)
        grid.attach_next_to(self.play_now, self.toggle_playpause, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.output_text, self.add_to_playlist, Gtk.PositionType.BOTTOM, 4, 1)
        
        # Using the following line, we will catch the Enter key pressed
        self.youtube_entry.connect("activate", self.on_play_now)
        self.progresseventbox.connect("button-press-event", self.on_mouse_click)
        self.add_to_playlist.connect("clicked", self.on_add_link)
        self.toggle_fullscreen.connect("clicked", self.on_fullscreen_toggle)
        self.toggle_playpause.connect("clicked", self.on_toggle_playpause)
        self.play_now.connect("clicked", self.on_play_now)

        self.timeout_id = GObject.timeout_add(1000, self.on_get_percentage, None)

    #def on_mouse_click(progressbar, widget, event):
    def on_mouse_click(self, widget, event):
    # The _widget is used in sonata, but what does it mean?    
    #def on_mouse_click(self, _widget, event):
        width = self.progresseventbox.get_allocated_width()
        #allocation = progressbar.get_allocation()
        #print(allocation)
        #print(allocation.width)
        #width = self.progressbar.get_allocated_width()
        # is this correction because of the set_border_width or set row / column spacing?
        # it is roughly 18 pt greater then the furthest point I can reach with the mouse
        #width = width - 18
        print(width)
        #path = self.get_path_at_pos(event.x, event.y)
        #print(path)
        print(event.x, event.y)
        percentage = event.x / width * 100
        # does it get rounded in python3 ?
        #percentage = int(percentage)
        print(percentage)
        percentage = str(percentage)
        output = (subprocess.check_output(["kodi-cli", "-g", percentage]))
        # Let's get some response from kodi-cli
        output = (subprocess.check_output(["kodi-cli", "-g"]))
        output = output.decode('ascii')
        # http://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string
        self.output_text.set_text(output)

    def on_get_percentage(self, user_data):
        self.percentage = (subprocess.check_output(["kodi-cli","-r"]))
        self.percentage = (self.percentage.decode('ascii'))
        self.percentage = self.percentage.rstrip()
        print("antes"+self.percentage+"después")
        # Acording to following link, if not is the prefered way of finding out empty strings as they are "falsy"
        # http://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
        if not self.percentage :
            self.percentage = 0
            print(self.percentage)
            self.progressbar.set_fraction(0)
            self.progressbar.set_text("Kodi is not playing at the moment")
            return True
        else:
            pass
        self.percentage = float(self.percentage)
        #try:
        #    self.percentage = float(self.percentage)
        #except:
        #    self.percentage = 0
        self.percentage = int(self.percentage)
        self.percentage = self.percentage/100
        #type(self.percentage)
        print(self.percentage)
        # As this is a timeout function, return True so that it
        # continues to get called
        self.progressbar.set_fraction(self.percentage)
        output = (subprocess.check_output(["kodi-cli", "-g"]))
        output = output.decode('ascii')
        # http://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string
        output = output[:-1]
        output = output.lstrip("Playing from ")
        self.progressbar.set_text(output)
        #self.progressbar.set_show_text(True)
        #print(output)
        return True

    def on_add_link(self, widget):
        #output = (subprocess.check_output(["kodi-cli", "-q", self.clipboard_value]))
        # let us use what is actually in the entry field and we are seeing, not what is in the clipper
        output = (subprocess.check_output(["kodi-cli", "-q", self.youtube_entry.get_text()]))
        output = (output.decode('ascii'))
        self.output_text.set_text(output)
        return True

    def on_fullscreen_toggle(self, widget):
        #output=(subprocess.call(["kodi-cli","-f"]))
        output = (subprocess.check_output(["kodi-cli","-f"]))
        output = (output.decode('ascii'))
        self.output_text.set_text(output)
        return True

    def on_toggle_playpause(self, widget):
        #output=(subprocess.call(["kodi-cli","-f"]))
        output = (subprocess.check_output(["kodi-cli","-p"]))
        output = (output.decode('ascii'))
        self.output_text.set_text(output)
        return True

    def on_play_now(self, widget):
        #output = (subprocess.check_output(["kodi-cli", "-y", self.clipboard_value]))
        # let us use what is actually in the entry field and we are seeing, not what is in the clipper
        output = (subprocess.check_output(["kodi-cli", "-y", self.youtube_entry.get_text()]))
        print(output)
        output = (output.decode('ascii'))
        self.output_text.set_text(output)
        # We need to put return True in order to keep the loop running after we call this function.
        return True

    def on_espace_press(self, widget, event):
        #print(event.keyval)
        # Following will quit the Window on pressing Espace 
        # we got the value from the previous line
        if event.keyval == 65307 :
             Gtk.main_quit()


win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.connect('key-press-event', win.on_espace_press)
win.show_all()
Gtk.main()
