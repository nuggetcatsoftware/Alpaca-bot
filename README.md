# Alpaca-bot

A bot used by the OGs, mainly a music bot.

# Installation

Run 
```
pip install -r requirements.txt
```
and run run.py

# Supported links for -play

Youtube, SoundCloud, Spotify, Bandcamp, Twitter, and custom files.

# Prerequisites:

#### API Keys
* Discord - https://discord.com/developers
* Spotify (optional) - https://developer.spotify.com/dashboard/
  - Client ID
  - Client Secret
  - Note: Limited to 50 playlist items without API

Obtained keys must be entered into ```config/config.py```
* FFmpeg.exe (included)

# Issues and contributing

reference don't ask to ask to ask and write proper  

# Commands:

### Music

After the bot has joined your server, use ```$help``` to display help and command information.


```
$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]
```

* Plays the audio of supported website
    - A link to the video (https://ww...)
    - The title of a video ex. (Gennifer Flowers - Fever Dolls)
    - A link to a YouTube playlist
* If a song is playing, it will be added to queue

```
$skip / $s
```

* Skips the current song and plays next in queue.

```
$q
```

* Show the list of songs in queue

```
$shuffle /$sh
```

* Shuffle the queue

```
$l / $loop
```

* Loop the current playing song, toggle on/off

```
$pause
```

* Pauses the current song.

```
$resume
```

* Resumes the paused song.

```
$prev
```

* Goes back one song and plays the last song again.

```
$np
```

* Shows more details about the current song.

```
$volume / $vol
```

* Adjust the volume 1-100%
* Pass no arguments for current volume

```
$stop / $st
```
* Stops the current song and clears the playqueue.


### General

```
$settings /$setting/ $set
```
* No Arguments: Lists server settings
* Arguments: (setting) (value)
* Use "unset" as an argument to reset a setting
* Example: $setting start_voice_channel ChannelName
* Administrators only

```
$c
```

* Connects the bot to the user's voice channel

```
$cc
```

* Switch the bot to the user's voice channel

```
$dc
```

* Disconnects the bot from the current voice channel

```
$history
```
* Shows you the titles of the X last played songs. Configurable in config.config.py


### Utility

```
$reset / $rs
```

* Disconnect and reconnect to the voice channel

```
$ping
```

* Test bot connectivity

```
$addbot
```

* Displays information on how to add the bot to another server of yours.

