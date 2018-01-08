import random
import time
import rtmidi

midiout = rtmidi.MidiOut()
# available_ports = midiout.get_ports()
midiout.open_port(0)

# full = .3

long = .13
short = .1


def sendMidi(num, length, velocity=100):
    velocity = [0xb0, 0x29, velocity]
    note_on = [0x90, num, 1]
    note_off = [0x80, num, 0]
    midiout.send_message(velocity)
    midiout.send_message(note_on)
    time.sleep(length)
    midiout.send_message(note_off)

# del midiout
