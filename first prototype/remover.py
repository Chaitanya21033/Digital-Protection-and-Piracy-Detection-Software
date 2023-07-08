import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# parameters
path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\sample_cut.wav"
path2 = "C:\\Users\\om\\Desktop\\anti piracy\\sample_out.wav"
cutoff = 17000  # desired cutoff frequency of the filter, Hz
order = 6       # order of the filter

# load wav file
fs, data = wavfile.read(path)  # read wav file

# check if audio file is stereo (2 channels)
if len(data.shape) > 1 and data.shape[1] > 1: 
    # apply filter to each channel separately
    channels = []
    for channel in range(data.shape[1]):
        filtered_channel = butter_lowpass_filter(data[:, channel], cutoff, fs, order)
        channels.append(filtered_channel)
    filtered_data = np.column_stack(channels)
else:
    filtered_data = butter_lowpass_filter(data, cutoff, fs, order)

# save filtered data to wav file
wavfile.write(path2, fs, filtered_data.astype(np.int16))  # write filtered data to wav file
