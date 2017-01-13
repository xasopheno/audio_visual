##Synopsis

triangles.py

Given two vector lengths, if the two lengths are in
    the desired ratio, generate two tones at with 
    frequencies corresponding to vector length. 
    Currently set up to detect Perfect 5ths or the ratio 3/2
Vector lengths should probably be scaled to 
    the range(30, 2000)
A time.sleep() function is slowing down the execution 
    of this script for viewability. 
Using PyAudio for sound. I'm still having a problem with 
    pops due to concantenated audio. Perhaps you can figure
    something out. 
    http://stackoverflow.com/questions/36438850/how-to-remove-pops-from-concatented-sound-data-in-pyaudio

## Dependencies

PyAudio - Python Bindings for PortAudio

install with:
  python -m pip install pyaudio

## Use
  To run, type:
     python triangles.py
