import numpy as np
from scipy.io.wavfile import read
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# read the wav file
path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\oracle.wav"   
rate, data = read(path)

# Make sure it's mono by taking the first channel only
if len(data.shape) > 1:
    data = data[:, 0]

# list of frequencies to search
# frequencies_to_search = [20000, 20500, 21000, 21500, 22000]
frequencies_to_search = [17000, 20250, 20500, 20750, 21000]  # in Hz

# FFT parameters
window_size = 10000  # size of the FFT wi ndow, adjust as needed
overlap = 0.05 # overlap between windows, adjust as needed

# list to store the results
results = {freq: [] for freq in frequencies_to_search}

# Perform the FFT and search for the frequencies
window_step = int(window_size * (1 - overlap))
for window_start in range(0, len(data) - window_size, window_step):
    window_end = window_start + window_size
    window_data = data[window_start:window_end]

    # Perform the FFT
    spectrum = np.abs(fft(window_data)[:window_size // 2])
    freqs = np.fft.fftfreq(window_size, 1 / rate)[:window_size // 2]

    # Search for the frequencies
    for frequency in frequencies_to_search:
        # Find the closest frequency in the FFT result
        closest_freq_index = np.argmin(np.abs(freqs - frequency ))

        # If the amplitude of this frequency is above a certain threshold, record it
        # You may want to adjust this threshold for your specific use case
        if spectrum[closest_freq_index] > 1e6:  
            results[frequency].append(window_start / rate)  # convert samples to seconds

# Print the results
for frequency, timestamps in results.items():
    print(f'Frequency {frequency}Hz found at timestamps: {timestamps} seconds')
