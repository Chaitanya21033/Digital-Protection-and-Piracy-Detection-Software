import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Load the audio file
# path = "C:\\Users\\om\\Desktop\\test.wav"
# path = "C:\\Users\\om\\Desktop\\anti piracy\\sample_out.wav"
path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\testing.wav"
# path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\sample_cut3_rec.wav"

audio_data, sample_rate = librosa.load(path, sr=None)

# Compute the Short-Time Fourier Transform (STFT)
stft_result = librosa.stft(audio_data)

# Compute the power     spectral density (squared magnitude of STFT)
psd = np.abs(stft_result) ** 2

# Convert the power spectral density to Decibels (log scale)
psd_db = librosa.power_to_db(psd, ref=np.max)

# Plotting the spectrogram
plt.figure(figsize=(14, 5))
librosa.display.specshow(psd_db, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()
