kodi-cli
========

Kodi/XBMC bash script to send Kodi commands using JSON RPC. It also allows sending YouTube videos to Kodi.

## Usage

`kodi-cli -[p|i|s|(y|q) youtube URL/ID|t "text to send"|o "youtube title"]`

# Setup

You must either put your Kodi setup (found under "Interfaces") in the first few lines of the script itself, or put a file named .kodirc in your $HOME directory. This file (example provided) contains only four lines in *this specific order*:

```
The Kodi Host
The port Kodi listens on (the webserver port)
Username
Password
```

# Arguments
```
 -p Play/Pause the current played video
 -s Stop the current played video
 -y play YouTube video. Use either URL/ID (of video)
 -q queue YouTube video to the current list. Use either URL/ID (of video). Use instead of -y.
 -o play YouTube video directly on Kodi. Use the name of video.
 -v interactive volume control
 -i interactive navigation mode. Accept keyboard keys of Up, Down, Left, Right, Back,
    Context menu and information
 -t 'text to send'
 -u Increment the volume on Kodi
 -d Decrement the volume on Kodi
 -f toggle fullscreen
 -m Update libraries
 -n clean libraries
 -h showing this help message

```

## Dependencies

* curl
* Kodi

# Optional dependencies

* [mps-youtube](https://github.com/np1/mps-youtube) on the machine running Kodi for the -o option to work.

