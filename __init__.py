import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
tempo = mido.bpm2tempo(90)


NOTE_NAME_TO_NUMBER = {
    'C0': 12, 'C#0': 13, 'D0': 14, 'D#0': 15, 'E0': 16, 'F0': 17, 'F#0': 18, 'G0': 19, 'G#0': 20, 'A0': 21, 'A#0': 22, 'B0': 23,
    'C1': 24, 'C#1': 25, 'D1': 26, 'D#1': 27, 'E1': 28, 'F1': 29, 'F#1': 30, 'G1': 31, 'G#1': 32, 'A1': 33, 'A#1': 34, 'B1': 35,
    'C2': 36, 'C#2': 37, 'D2': 38, 'D#2': 39, 'E2': 40, 'F2': 41, 'F#2': 42, 'G2': 43, 'G#2': 44, 'A2': 45, 'A#2': 46, 'B2': 47,
    'C3': 48, 'C#3': 49, 'D3': 50, 'D#3': 51, 'E3': 52, 'F3': 53, 'F#3': 54, 'G3': 55, 'G#3': 56, 'A3': 57, 'A#3': 58, 'B3': 59,
    'C4': 60, 'C#4': 61, 'D4': 62, 'D#4': 63, 'E4': 64, 'F4': 65, 'F#4': 66, 'G4': 67, 'G#4': 68, 'A4': 69, 'A#4': 70, 'B4': 71,
}


def note_name_to_number(note_name):
    return NOTE_NAME_TO_NUMBER[note_name]


last_tick = 0  # Variable to keep track of the last tick position

def add_note(measure, beat, note, velocity, duration):
    global last_tick
    # Convert the measure, beat, and division into ticks (assuming 480 ticks per beat)
    start_tick = round(((measure - 1) * 4 + beat - 1) * 480)
    duration_tick = round(duration * 480)
    # Convert note name to MIDI note number
    note_number = note_name_to_number(note)
    # Add the note on and note off messages
    track.append(Message('note_on', note=note_number,
                 velocity=velocity, time=start_tick - last_tick))
    track.append(Message('note_off', note=note_number,
                 velocity=velocity, time=duration_tick))
    last_tick = start_tick + duration_tick



# Input data
# (measure number, beat start, note name, velocity, duration)

melody_data = [
    (1, 1, 'D4', 83, 1),
    (1, 2, 'F#4', 83, 1),
    (1, 3, 'E4', 83, 2),

    (2, 1, 'B3', 83, 1),
    (2, 2, 'D4', 83, 1),
    (2, 3, 'B3', 83, 2),

    (3, 1, 'A3', 83, 1),
    (3, 2, 'C#4', 83, 1),
    (3, 3, 'A3', 83, 2),

    (4, 1, 'B3', 83, 1),
    (4, 2, 'D4', 83, 1),
    (4, 3, 'B3', 83, 2),

    # Chorus
    (5, 1, 'D4', 83, 0.5),
    (5, 1.5, 'E4', 83, 0.5),
    (5, 2, 'F#4', 83, 2),

    (6, 1, 'B3', 83, 1),
    (6, 2, 'D4', 83, 0.5),
    (6, 2.5, 'E4', 83, 1.5),

    (7, 1, 'F#4', 83, 1),
    (7, 2, 'A4', 83, 0.5),
    (7, 2.5, 'F#4', 83, 1.5),

    (8, 1, 'E4', 83, 1),
    (8, 2, 'D4', 83, 0.5),
    (8, 2.5, 'C#4', 83, 0.5),
    (8, 3, 'B3', 83, 1)
]



# Add each note to the MIDI track
for d in melody_data:
    add_note(*d)

track.append(MetaMessage('set_tempo', tempo=tempo))
# Save the MIDI file
mid.save('output_file.mid')
