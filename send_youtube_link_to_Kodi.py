#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
# only needed for the exit confirmation dialog
#from tkinter import messagebox
import subprocess

def close_window(*args):
    root.destroy()

# The following adds a exit confirmation dialog
#def on_closing():
#        if messagebox.askokcancel("Quit", "Do you want to quit?"):
#                    root.destroy()
                    
#def play(*args):
#    try:
#        value = float(youtube_link.get())
#        output_text.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#    except ValueError:
#        pass

def add(*args):
    output=(subprocess.check_output(["kodi-cli", "-q", clipboard_value]))
    output_text.set(output)

def fullscreen_toggle(*args):
    #output=(subprocess.call(["kodi-cli","-f"]))
    output=(subprocess.check_output(["kodi-cli","-f"]))
    output_text.set(output)

def toggle_playpause(*args):
    #output=(subprocess.call(["kodi-cli","-f"]))
    output=(subprocess.check_output(["kodi-cli","-p"]))
    output_text.set(output)

def play(*args):
    # print commands used to debug
    #print(clipboard_value)
    #print(str(youtube_link))
    clipboard_value=youtube_link.get()
    #print(clipboard_value)
    output=(subprocess.check_output(["kodi-cli", "-y", clipboard_value]))
    #print(output.decode('ascii'))
    output_text.set(output)

root = Tk()
root.title("Play YouTube link on Kodi")
# using kodi-cli 

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

youtube_link = StringVar()
output_text = StringVar()

# the following gets only the CLIPBOARD clipboard (Control + C)
#clipboard_value = root.clipboard_get()

try:
    clipboard_value=subprocess.check_output(["xclip", "-o"])
except:
    clipboard_value=bytes()
# To fix the strange output I was getting
# http://stackoverflow.com/questions/15374211/why-does-popen-communicate-return-bhi-n-instead-of-hi
# The b indicates that what you have is bytes, which is a binary sequence of bytes rather than a string of Unicode characters.
# The bytes type is not directly print()able, so you're being shown the repr of the bytes you have. 
# If you know the encoding of the bytes you received from the subprocess, you can use decode() to convert them into a printable str

try:
    clipboard_value=(clipboard_value.decode('ascii'))
except:
    clipboard_value=bytes()

youtube_link.set(clipboard_value)

youtube_link_entry = ttk.Entry(mainframe, width=7, textvariable=youtube_link)
youtube_link_entry.grid(column=1, row=1, columnspan=4, sticky=(W, E))

ttk.Button(mainframe, text="Add link to playlist", command=add).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Toggle fullscreen", command=fullscreen_toggle).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="Toggle Play/Pause", command=toggle_playpause).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Play link now", command=play).grid(column=4, row=2, sticky=W)

ttk.Label(mainframe, textvariable=output_text).grid(column=1, row=3, columnspan=4, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

youtube_link_entry.focus()
root.bind('<Return>', play)
root.bind('<Escape>', close_window)

# Uncommented the following for exit confirmation dialog
#root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
