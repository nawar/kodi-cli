"kodi-cli" and its simple GTK3 frontend
=======================================

Kodi/XBMC bash script to send Kodi commands using JSON RPC. It also allows sending youtube videos to Kodi. The GTK3 frontend simpliefies sending YouTube links and controling basic aspects of playback withing X. 

#Usage

`kodi-cli -[p|i|s|(y|q) youtbe URL/ID|t "text to send"|o "youtube title"]`

#Arguments
```
 -d Decrement the volume on Kodi
 -f toggle fullscreen
 -g go to specified percentage of the video
 -h showing this help message
 -i interactive navigation mode. Accept keyboard keys of Up, Down, Left, Right, Back,
 	Context menu and information
 -n play next item in current playlist
 -o play youtube video directly on Kodi, use the name of video (this option depends on using mps-youtube)
 -p Play/Pause the current played video
 -q queue youtube video to the current list, use either URL or ID (of video); use instead of -y
 -r retreive the percentage of the total time that has been played already
 -s stop the playback
 -t 'text to send'
 -u increment the volume on Kodi
 -y play youtube video; use either URL or ID (of video)
 -z suspend the system with Kodi

```

#Dependencies
for the "-o" option to work you'll need to install [mps-youtube](https://github.com/np1/mps-youtube)

#Version
1.1
