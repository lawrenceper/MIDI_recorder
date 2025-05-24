# Simple MIDI Recorder
## enhanced by @lawrenceper to provide some MIDI Recording functionality.
 :notes: MIDI recorder tool. Record and save a stream of midi input as a midi file.

###### (Developed as a support tool for the [CodeKlavier](https://codeklavier.space))

## Changes from the Original

This is a fork of [Narcode's MIDI Recorder] (https://github.com/narcode/MIDI_recorder). I've made the following changes, ensuring that visually impaired individuals have access to a cross platform MIDI recorder:

It is now possible to set the MIDI tempo before recording. This is so that if you decide to send your performances to accessible sheet music software like MuseScore or another accessible music editor, the tempo will be correctly set and interpreted.

It is now possible to have the program Wait for a specific amount of time before starting recording. This is so that to find your way to the keyboard before recording starts, getting rid of unnecessary silence before you play.

## To Do:

- A minimal metronome that plays during recording, possibly using numpi and sounddevice

## instructions

- make sure you have python3 installed
- pip3 install python-rtmidi
- pip3 install mido

## then simply run in terminal:

`python3 recorder.py`

CodeKlavier is developed thanks to the support of **Stimuleringsfonds Creatieve Industrie**
