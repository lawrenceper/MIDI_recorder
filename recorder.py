import time
import rtmidi
#import from parrentdir
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from CK_rec.setup import Setup
from CK_rec.rec_classes import CK_rec
from mido import MidiFile, MidiTrack, Message, MetaMessage


# Start the Device
codeK = Setup()
myPort = codeK.perform_setup()
codeK.open_port(myPort)
on_id = codeK.get_device_id()
print('your note on id is: ', on_id)

# Ask the user for the tempo of the recorded MIDI track (Default 120)
try:
    tempo = int(input("Please enter the tempo of your new MIDI recorded track (Default 120BPM)."))
    assert tempo > 0, "Oops! The tempo can't be 0 or a negative number"
except:
    tempo = 120 # Set tempo to the defaults.

# Asks if the start of the recording should be delayed.
try:
    delay = float(input("Would you like the recording to start automatically after a delay? Leave blank for no delay."))
    assert delay >= 0, "Oops! The delay can't be a negative value."
except:
    delay = 0 # Set delay to 0, no delay and auto-start recording

# record
midiRec = CK_rec(myPort, on_id, tempo=tempo, delay=delay, debug=False)
codeK.set_callback(midiRec)


# Loop to program to keep listening for midi input
try:
    while True:
        time.sleep(0.001)
except KeyboardInterrupt:
    print('')
finally:
    name = input('\nsave midi recording as? (leaving the name blank discards the recording): ')
    if name != "":
        midiRec.saveTrack(name)
    codeK.end()
