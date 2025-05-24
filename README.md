# Simple MIDI Recorder
## New features and enhancements by @lawrenceper.
 :notes: MIDI recorder tool. Record and save a stream of midi input as a midi file.

###### (Developed as a support tool for the [CodeKlavier](https://codeklavier.space))

## Changes from the Original

This is a fork of [Narcode's MIDI Recorder](https://github.com/narcode/MIDI_recorder). I've made the following enhancements, ensuring that visually impaired individuals have access to a cross platform MIDI recorder:

- You can now set the MIDI tempo before recording, so that your performance is easily interpreted by your DAW or sheet music software.
- the program can Wait for a specific amount of time before the recording starts. It's useful when your piano keyboard is across the room.

## To Do:

- A minimal metronome that plays during recording, possibly using numpi and sounddevice

## instructions

- make sure you have python3 installed
- pip3 install python-rtmidi
- pip3 install mido

## then simply run in terminal:

`python3 recorder.py`

CodeKlavier is developed thanks to the support of **Stimuleringsfonds Creatieve Industrie**
