# import numpy as np
# import matplotlib.pyplot as plt
# import librosa
# from scipy import fftpack

# # Load the audio file
# path = "C:\\Users\\om\\Desktop\\anti piracy\\sample_cut3.mp3" # path of the audio file "
# audio_data, sample_rate = librosa.load(path)

# # Compute the Short-Time Fourier Transform (STFT)
# stft_result = librosa.stft(audio_data)

# # Compute the power spectral density (squared magnitude of STFT)
# psd = np.abs(stft_result) ** 2

# # Convert the power spectral density to Decibels (log scale)
# psd_db = librosa.power_to_db(psd, ref=np.max)

# # Plotting the spectrogram
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(psd_db, sr=sample_rate, x_axis='time', y_axis='hz')
# plt.colorbar(format='%+2.0f dB')
# plt.title('Spectrogram')
# plt.show()

# # waveform
# # audio, sr = librosa.load(path)
# # time = np.arange(0, len(audio)) / sr
# # plt.figure(figsize=(14, 5))
# # plt.plot(time, audio)
# # plt.title('Waveform')
# # plt.xlabel('Time (seconds)')
# # plt.show()

# #  spectrogram

# # audio, sr = librosa.load(path)
# # X = librosa.stft(audio)
# # Xdb = librosa.amplitude_to_db(abs(X))
# # plt.figure(figsize=(14, 5))
# # librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# # plt.colorbar()
# # plt.title('Spectrogram')
# # plt.show()

# # mel spectrogram
# # audio, sr = librosa.load(path)
# # spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, fmax=8000)
# # spectrogram = librosa.power_to_db(spectrogram)
# # plt.figure(figsize=(14, 5))
# # librosa.display.specshow(spectrogram, sr=sr, x_axis='time', y_axis='mel', fmax=8000)
# # plt.colorbar(format='%+2.0f dB')
# # plt.title('Mel Spectrogram')
# # plt.show()

# # chromogram

# # audio, sr = librosa.load(path)
# # chroma = librosa.feature.chroma_stft(y=audio, sr=sr, hop_length=100)
# # plt.figure(figsize=(14, 5))
# # librosa.display.specshow(chroma, x_axis='time', y_axis='chroma', hop_length=100, cmap='coolwarm')
# # plt.title('Chromagram')
# # plt.show()

# # zero crossing data

# # audio_data, sample_rate = librosa.load(path)
# # n0 = 9000
# # n1 = 9100
# # plt.figure(figsize=(14, 5))
# # plt.plot(audio_data[n0:n1])
# # plt.grid()
# # zero_crossings = librosa.zero_crossings(audio_data[n0:n1], pad=False)
# # print(sum(zero_crossings)) 

# # spectral contrast


# # Load the audio file
# # audio_data, sample_rate = librosa.load(path)

# # # Compute the STFT of the audio signal
# # stft_audio = librosa.stft(audio_data)

# # # Compute the spectral contrast
# # spectral_contrast = librosa.feature.spectral_contrast(S=np.abs(stft_audio), sr=sample_rate)

# # # Plot the spectral contrast
# # plt.figure(figsize=(15, 5))
# # librosa.display.specshow(spectral_contrast, sr=sample_rate, x_axis='time')
# # plt.colorbar()
# # plt.ylabel('Frequency Bands')
# # plt.title('Spectral contrast')
# # plt.show()

# # tonnetz

# # audio_data, sample_rate = librosa.load(path)
# # tonnetz = librosa.effects.harmonic(audio_data)
# # tonnetz = librosa.feature.tonnetz(y=tonnetz, sr=sample_rate)
# # plt.figure(figsize=(15, 5))
# # librosa.display.specshow(tonnetz, sr=sample_rate, x_axis='time')
# # plt.colorbar()
# # plt.title('Tonnetz')
# # plt.show()

# # tempogram


# # audio_data, sample_rate = librosa.load(path)
# # hop_length = 512
# # oenv = librosa.onset.onset_strength(audio_data, sr=sample_rate, hop_length=hop_length)
# # tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sample_rate,
# #                                       hop_length=hop_length)
# # plt.figure(figsize=(15, 5))
# # librosa.display.specshow(tempogram, sr=sample_rate, x_axis='time')
# # plt.colorbar()
# # plt.title('Tempogram')
# # plt.show()

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from scipy import fftpack

# Load the audio file
path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\samplecut.wav" # path of the audio file
# path = "C:\\Users\\om\\Desktop\\anti piracy\\experimenting\\sample_0.wav" # path of the audio file
# path = "C:\\Users\\om\\Desktop\\anti piracy\\experimenting\\sample_1.wav" # path of the audio file
# path = "C:\\Users\\om\\Desktop\\anti piracy\\newfile.wav" # path of the audio file
# path = "C:\\Users\\om\\Desktop\\anti piracy\\newfile_conv.wav" # path of the audio file
audio_data, sample_rate = librosa.load(path, sr=None)

# Compute the Short-Time Fourier Transform (STFT)
stft_result = librosa.stft(audio_data)

# Compute the power spectral density (squared magnitude of STFT)
psd = np.abs(stft_result) ** 2

# Convert the power spectral density to Decibels (log scale)
psd_db = librosa.power_to_db(psd, ref=np.max)

# Plotting the spectrogram
plt.figure(figsize=(14, 5))
librosa.display.specshow(psd_db, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()


# # waveform
# audio, sr = librosa.load(path)
# time = np.arange(0, len(audio)) / sr
# plt.figure(figsize=(14, 5))
# plt.plot(time, audio)
# plt.title('Waveform')
# plt.xlabel('Time (seconds)')
# plt.show()