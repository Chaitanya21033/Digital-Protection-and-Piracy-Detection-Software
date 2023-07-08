import librosa
import numpy as np
import scipy.signal

file2 = "C:\\Users\\om\\Desktop\\anti piracy\\reclouder.wav" # path of the audio file
file1 = "C:\\Users\\om\\Desktop\\anti piracy\\rec.wav" # path of the audio file
# Load the two audio files

# Load the audio files with librosa
y1, sr1 = librosa.load(file1)
y2, sr2 = librosa.load(file2)

# Calculate the decibel difference
D1 = librosa.amplitude_to_db(np.abs(librosa.stft(y1)), ref=np.max)
D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y2)), ref=np.max)
db_diff = np.average(D1) - np.average(D2)
print(f'Decibel difference: {db_diff} dB')

# Calculate the pitch difference
fmin = librosa.note_to_hz('C2')
fmax = librosa.note_to_hz('C7')
pitches1, magnitudes1 = librosa.piptrack(y=y1, sr=sr1, fmin=fmin, fmax=fmax)
pitches2, magnitudes2 = librosa.piptrack(y=y2, sr=sr2, fmin=fmin, fmax=fmax)
pitch1 = pitches1[magnitudes1 > np.median(magnitudes1)]
pitch2 = pitches2[magnitudes2 > np.median(magnitudes2)]
pitch_diff = np.average(pitch1) - np.average(pitch2)
print(f'Pitch difference: {pitch_diff} Hz')

# Calculate the frequency spectrum difference
f1, Pxx_den1 = scipy.signal.periodogram(y1, sr1)
f2, Pxx_den2 = scipy.signal.periodogram(y2, sr2)
freq_diff = np.average(Pxx_den1) - np.average(Pxx_den2)
print(f'Frequency spectrum difference: {freq_diff}')
