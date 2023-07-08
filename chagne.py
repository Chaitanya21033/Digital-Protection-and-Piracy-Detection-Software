import numpy as np
from scipy.io.wavfile import read, write

def increase_volume_db(filename, decibel_difference):
    # Convert dB difference to a multiplication factor
    increase_ratio = np.power(10, decibel_difference / 20)

    # Read file
    rate, data = read(filename)
    
    # Detect data type
    dtype = data.dtype
    
    # Increase volume
    louder_data = data * increase_ratio

    # Clip values to prevent overflow
    if dtype == np.int16:
        louder_data = np.clip(louder_data, -32768, 32767)
    elif dtype == np.int32:
        louder_data = np.clip(louder_data, -2147483648, 2147483647)

    # Save as new file
    write(filename , rate, louder_data.astype(dtype))

file1 = "C:\\Users\\om\\Desktop\\anti piracy\\rec.wav" # path of the audio 

increase_volume_db(file1, 11.031925201416016)  # Increase volume by 10 dB



# import numpy as np
# import soundfile as sf
# import librosa

# # Constants - these would be your difference values
# db_difference = 11.031925201416016
# pitch_difference = 473.5531005859375
# freq_spec_difference = -1.2329954870438087e-06

# def adjust_db(audio_data, db_difference):
#     # This function increases or decreases the decibel level of the audio
#     factor = np.power(10., db_difference / 20.)
#     return audio_data * factor



# def adjust_freq_spectrum(audio_data, freq_spec_difference):
#     # This function adjusts the frequency spectrum of the audio
#     # It's a bit more complex, so this is a placeholder for the actual implementation
#     return audio_data + freq_spec_difference

# def hz_to_note(frequency):
#     # Convert frequency in Hz to a MIDI note number
#     return 12 * np.log2(frequency / 440) + 69

# def note_to_hz(note):
#     # Convert a MIDI note number to frequency in Hz
#     return 440 * np.power(2, (note - 69) / 12)

# def adjust_pitch(audio_data, sr, pitch_difference):
#     # Estimate the pitch of the audio data and convert it to a MIDI note
#     original_note = hz_to_note(librosa.pitch.tuning(audio_data, sr))
#     # Calculate the note that's a certain difference away
#     target_note = original_note + hz_to_note(pitch_difference)
#     # Calculate the difference in semitones
#     n_steps = target_note - original_note
#     # Shift the pitch of the audio data
#     return librosa.effects.pitch_shift(audio_data, sr, n_steps)


# # Load the second audio file
# file = "C:\\Users\\om\\Desktop\\anti piracy\\rec.wav" # path of the audio file
# audio_data, sr = librosa.load(file, sr=None)

# # Adjust dB, pitch and frequency spectrum
# audio_data = adjust_db(audio_data, db_difference)
# # audio_data = adjust_pitch(audio_data, sr, pitch_difference)
# # audio_data = adjust_freq_spectrum(audio_data, freq_spec_difference)

# # Write back the audio data into a .wav file
# sf.write("C:\\Users\\om\\Desktop\\anti piracy\\new_file.wav", audio_data, sr)
