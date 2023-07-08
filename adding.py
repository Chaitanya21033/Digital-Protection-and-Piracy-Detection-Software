import numpy as np
from scipy.io.wavfile import read, write

# read the wav file
path = "C:\\Users\\om\\Desktop\\anti piracy\\experimenting\\sample.wav"  # path of the audio file 

rate, data = read(path)

# Make sure it's mono by taking the first channel only
if len(data.shape) > 1:
    data = data[:, 0]

# specify the frequency of the sine wave (in Hz)
frequency = 20000

# specify the duration and interval of the sine wave
sine_duration = 0.001  # sine wave duration in seconds
sine_interval = 2  # interval between sine waves in seconds

# calculate the number of intervals in the audio file
num_intervals = int(len(data) / (rate * sine_interval))

# generate the sine wave and mix it into the audio at each interval
for i in range(num_intervals):
    # generate the time array for the sine wave
    start_time = i * sine_interval  # start time in seconds
    end_time = start_time + sine_duration  # end time in seconds
    time = np.arange(start_time, end_time, 1/rate)

    # generate the sine wave
    sine_wave = np.sin(2 * np.pi * frequency * time)

    # Apply a window function to the sine wave
    window = np.hanning(len(sine_wave))
    sine_wave = sine_wave * window

    # normalize sine wave to match original data amplitude
    sine_wave = sine_wave * np.max(np.abs(data))

    # calculate the start and end indices in the data array
    start_index = int(start_time * rate)
    end_index = int(end_time * rate)

    # make sure the end_index does not exceed the data length
    if end_index > len(data):
        end_index = len(data)

    # mix the original data with the sine wave
    data[start_index:end_index] += sine_wave[:end_index - start_index].astype(data.dtype)

out = "C:\\Users\\om\\Desktop\\anti piracy\\experimenting\\sample_0.wav"  # path of the audio file 
# write the result to a new wav file
write(out, rate, data)
