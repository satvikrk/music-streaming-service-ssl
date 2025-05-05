# music-streaming-service-ssl
Created a secure, SSL-encrypted music streaming server in Python where clients can browse, stream, and control playback of songs remotely using terminal commands.

#  Secure Terminal-Based Music Streaming Server (Python + SSL)

A lightweight, terminal-based music streaming system built with Python. This project allows clients to securely connect to a server over SSL, browse a music library, stream selected tracks, and control playback — all from the command line.

##  Features

- SSL-encrypted communication between client and server
- Server-side music playback using `pygame`
- Auto-detection of songs from the `/music` folder
- List available songs by title and artist
- Playback control: `pause`, `resume`, `stop`
- Simple and interactive terminal interface

## Tech Stack

- **Python 3**
- **Socket Programming**
- **SSL/TLS encryption** via Python’s `ssl` module
- **Pygame** for music playback
