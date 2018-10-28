import pretty_midi

# Create a PrettyMIDI object
# Pretty MIDIオブジェクトを作る。
cello_c_chord = pretty_midi.PrettyMIDI()

# Create an Instrument instance for a cello instrument
# Instrument Instanceを作る。ここではCello

# 楽器名を入れると、対応するGeneral MIDI program numberを返してくれる
cello_program = pretty_midi.instrument_name_to_program('Cello')


# Instrument instanceをCelloとして作成
cello = pretty_midi.Instrument(program=cello_program)


# Iterate over note names, which will be converted to note number later
# メロディをNoteNameで記載していますが、後ほどNoteNumberに変換されます。

for note_name in ['C5', 'E5', 'G5','B5']:
    # Retrieve the MIDI note number for this note name
    # NoteNameからNote Numberを検索しています。
    note_number = pretty_midi.note_name_to_number(note_name)

    # Create a Note instance, starting at 0s and ending at .5s
    # NoteInstanceを作成します。音(pitch)の開始時間と終了時間、
    # velocityを定義します。
    note = pretty_midi.Note(
        velocity=100, pitch=note_number, start=0, end=4)

    # Add it to our cello instrument
    # 上記で作成したNoteInstanceをCelloInstrumentに加えます。
    cello.notes.append(note)


# Add the cello instrument to the PrettyMIDI object
# ChelloInstrumentをPrettyMIDIオブジェクトに加えます。
cello_c_chord.instruments.append(cello)


# Write out the MIDI data
# PrettyMIDIオブジェクトをMIDIファイルとして書き出しましょう。
cello_c_chord.write('cello-C-chord.mid')