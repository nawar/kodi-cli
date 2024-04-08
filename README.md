kodi-cli
========

Kodi/XBMC bash script to send Kodi commands using JSON RPC. It also allows sending YouTube videos to Kodi.

## Usage

A sample usage would be 

`kodi-cli -[p|i|s|(y|q) youtube URL/ID|t "text to send"|o "youtube title"]`

Please check the [Arguments](#arguments) section on how to use the rest of the available options.

## Setup

You must either put your Kodi setup (found under "Interfaces") in the first few lines of the script itself, or put a file named `.kodirc` in your `$HOME` directory. This file (example provided) contains only four lines in *this specific order*:

```
The Kodi Host
The port Kodi listens on (the webserver port)
Username
Password
```

If you don't want to add your kodi passwword, you might leave the password line empty and instead specify a command invocation in the next line that returns your password on stdout.


```
The Kodi Host
The port Kodi listens on (the webserver port)
Username

Commannd invocation that returns the password on stdout (e.g. pass mykodibox/kodi)
```

## Arguments
```
 -p Play/Pause the current played video
 -s Stop the current played video
 -j Skip forward in the current played video by 10 seconds. Use -j <seconds> to specify custom time
 -k Skip backward in the current played video by 10 seconds. Use -k <seconds> to specify custom time
 -y Play youtube video. Use either URL/ID (of video)
 -q Queue youtube video to the current list. Use either URL/ID (of video). Use instead of -y.
 -o Play youtube video directly on Kodi. Use the name of video.
 -v Interactive volume control
 -i Interactive navigation mode. Accept keyboard keys of Up, Down, Left, Right, Back,
    Context menu and information
 -l Play default playlist (most useful after using -q a few times)
 -t 'text to send'
 -r Send text from stdin to kodi
 -u Increment the volume on Kodi
 -d Decrement the volume on Kodi
 -x Mute/Unmute the volume on Kodi
 -f Toggle fullscreen
 -m Update libraries
 -n Clean libraries
 -h Showing this help message

```

## Dependencies

* [bash](https://www.gnu.org/software/bash/) version 4+
* [curl](https://curl.haxx.se/)
* [Kodi](https://kodi.tv/)

## Optional dependencies

* [mps-youtube](https://github.com/np1/mps-youtube) on the machine running Kodi for the -o option to work.

## Advanced usage

With the addition of a few other tools, most notably

* [youtube-dl](https://github.com/rg3/youtube-dl)
* [jq](https://github.com/stedolan/jq)
* [zenity](https://github.com/GNOME/zenity)
* awk (should be part of your distro).

You can create a dialog to download and sequentially (and with confirmation) play entire playlists - defaulting to your Watch Later playlist - on your Kodi, acting like a kind of remote "casting" program.  See the script **playlist_to_kodi** for an example.
