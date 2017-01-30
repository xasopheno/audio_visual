# Game of Life and Video

Renders a video where alive pixels in Conway's Game of Life are the pixels that are visible in the video. 

Imagine a Conway's Game of Life filter on a video. 

## Installation

brew install ffmpeg
pip install -r requirements.txt

## Run
- create 'video/' folder in the visual directory. 
use this command to separate a video into frames:
ffmpeg -i name_of_video.mp4 -r 30/1 $filename%04d.png

- python golvideo.py
