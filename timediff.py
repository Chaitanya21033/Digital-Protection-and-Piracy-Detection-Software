from scipy.io.wavfile import read
from scipy.signal import spectrogram
import numpy as np

path = "C:\\Users\\om\\Desktop\\anti piracy\\experimenting\\sample_0.wav" # path of the audio file

# Load the wav file
sample_rate, audio = read(path)

# Make sure audio is mono
if audio.ndim > 1:
    audio = np.mean(audio, axis=1)

# Calculate the spectrogram of the audio
frequencies, times, Sxx = spectrogram(audio, fs=sample_rate, nperseg=1024, noverlap=512, mode='magnitude')

# Find the index of the 20000Hz frequency
index_20000Hz = np.argmin(np.abs(frequencies - 20000))

# Find the times where the power at that frequency is above a certain threshold
# Here, we choose the threshold to be 20% of the maximum power at that frequency
threshold = 0.2 * np.max(Sxx[index_20000Hz])
timestamps = times[Sxx[index_20000Hz] > threshold]

# Print the timestamps
# timestamps = [round(timestamp, 2) for timestamp in timestamps]

    
